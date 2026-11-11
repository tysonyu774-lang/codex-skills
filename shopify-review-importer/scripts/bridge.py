"""Review Bridge: conservative, offline-first import preparation (stdlib only)."""
import argparse, csv, datetime as dt, hashlib, html, json, pathlib, re, sqlite3
from urllib.parse import urlparse


def identify(url):
    p = urlparse(url); host = (p.hostname or '').lower()
    if re.fullmatch(r'(www\.)?amazon\.(com|co\.uk|de|fr|ca|com\.au|co\.jp)', host):
        m = re.search(r'/(?:dp|gp/product)/([A-Z0-9]{10})(?:/|$)', p.path)
        return 'amazon', m.group(1) if m else ''
    if host in ('wayfair.com', 'www.wayfair.com'):
        return 'wayfair', p.path.rsplit('/', 1)[-1].removesuffix('.html')
    return 'unknown', ''


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def prepare(rows, config, db):
    db.execute('CREATE TABLE IF NOT EXISTS ledger (key TEXT PRIMARY KEY, fingerprint TEXT, state TEXT)')
    ready, issues, seen = [], [], set()
    for raw in rows:
        r = dict(raw); reasons = []
        platform, pid = identify(r.get('source_url', ''))
        r.update(source_platform=platform, source_product_id=pid,
                 collected_at=dt.datetime.now(dt.timezone.utc).isoformat(), target=config.get('target', {}))
        fp = digest([r.get(k, '') for k in ('body', 'author', 'date', 'rating', 'images')])
        key = digest([platform, pid, r.get('review_id') or fp, config.get('target'), config['plugin']])
        r.update(fingerprint=fp, ledger_key=key)
        old = db.execute('SELECT fingerprint,state FROM ledger WHERE key=?', (key,)).fetchone()
        if key in seen: reasons.append('duplicate_in_batch')
        seen.add(key)
        if old:
            if old[0] != fp: reasons.append('changed_review_requires_reconciliation')
            elif old[1] in ('submitted','unknown','confirmed'): reasons.append('historical_'+old[1])
        try:
            date = dt.date.fromisoformat(r.get('date', '')); r['normalized_date'] = date.isoformat()
        except (ValueError, TypeError): reasons.append('missing_or_invalid_date')
        if str(r.get('rating')) not in ('1','2','3','4','5'): reasons.append('invalid_rating')
        if not r.get('body'): reasons.append('missing_body')
        if config['plugin'] == 'judgeme' and len(r.get('body','')) > 5000: reasons.append('body_too_long')
        if config['plugin'] == 'loox' and not r.get('author'): reasons.append('missing_author')
        target = config.get('target', {})
        mapping = config.get('mappings', {}).get(r.get('source_url'))
        if not target.get('store') or not target.get('handle') or mapping != target: reasons.append('unconfirmed_product_mapping')
        if not config.get('reuse_authorized'): reasons.append('reuse_authorization_missing')
        images = r.get('images', [])
        if not isinstance(images, list): reasons.append('images_must_be_list'); images = []
        # Reachability evidence must be supplied by the collecting agent; never infer association.
        valid = []
        for im in images:
            if not isinstance(im, dict) or im.get('review_id') != r.get('review_id') or not r.get('review_id') or im.get('status') != 'verified_public' or not re.fullmatch(r'https://[^\s,]+\.(?:jpg|jpeg|png)', im.get('url',''), re.I):
                reasons.append('image_needs_verification')
            else: valid.append(im['url'])
        r['import_images'] = valid[:5]; r['omitted_images'] = valid[5:]
        r['issues'] = reasons
        r['status'] = 'pending' if reasons else 'validated'
        (issues if reasons else ready).append(r)
    return ready, issues


def export(rows, plugin, path, published=False):
    fields = ('product_handle rating author body created_at photo_url' if plugin == 'loox' else 'title body rating review_date reviewer_name reviewer_email product_handle picture_urls curated').split()
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader()
        for r in rows:
            common = dict(product_handle=r['target']['handle'], rating=r['rating'], body=r['body'])
            pics = ','.join(r['import_images'])
            if plugin == 'loox': common.update(author=r['author'], created_at=r['normalized_date'], photo_url=pics)
            else: common.update(title=r.get('title',''), review_date=dt.date.fromisoformat(r['normalized_date']).strftime('%d/%m/%Y'), reviewer_name=r.get('author',''), reviewer_email=r.get('email',''), picture_urls=pics, curated='ok' if published else 'not-yet')
            writer.writerow(common)


def main():
    p = argparse.ArgumentParser(); p.add_argument('--config', required=True); p.add_argument('--input'); p.add_argument('--url', action='append', default=[]); p.add_argument('--out', required=True); p.add_argument('--mode', choices=['prepare','apply'], default='prepare')
    a = p.parse_args(); c = json.loads(pathlib.Path(a.config).read_text()); out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.mode == 'apply': p.error('apply requires an authorized browser import and per-record reconciliation; no write API is implemented')
    rows = []
    if a.input:
        source = pathlib.Path(a.input)
        if source.suffix == '.json': rows = json.loads(source.read_text())
        elif source.suffix == '.csv':
            with source.open(encoding='utf-8-sig', newline='') as f: rows = list(csv.DictReader(f))
            for r in rows: r['images'] = json.loads(r.get('images') or '[]')
        else: p.error('Saved HTML must first be extracted into review-scoped JSON by the collecting agent')
    if c.get('plugin') not in ('loox','judgeme'): p.error('plugin must be loox or judgeme')
    db = sqlite3.connect(out/'ledger.sqlite3')
    ready, pending = prepare(rows, c, db)
    export(ready, c['plugin'], out/'import.csv', c.get('published', False))
    for r in ready: db.execute('INSERT OR IGNORE INTO ledger VALUES (?,?,?)',(r['ledger_key'],r['fingerprint'],'exported'))
    db.commit(); db.close()
    reports = [dict(url=u, platform=identify(u)[0], status='requires_user_input' if identify(u)[0]!='unknown' else 'unsupported', collected=0, displayed_total=None, stop_reason='No authorized live collection transport configured; use connected reader or authorized export') for u in a.url]
    report = dict(stage='待导入', collected=len(rows), exported=len(ready), pending=len(pending), confirmed=0, sources=reports, reviews=ready+pending)
    (out/'batch.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    (out/'preview.html').write_text('<meta charset="utf-8"><h1>评论导入预览（待导入）</h1>'+''.join('<pre>'+html.escape(json.dumps(r,ensure_ascii=False,indent=2))+'</pre>' for r in ready+pending))
    print(json.dumps({k:v for k,v in report.items() if k!='reviews'},ensure_ascii=False))

if __name__ == '__main__': main()
