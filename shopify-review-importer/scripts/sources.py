"""Deterministic saved-page adapters. Never execute page scripts."""
import datetime as dt
import json
import re
from bs4 import BeautifulSoup
from bridge import identify


def parse_page(url, markup):
    platform, pid = identify(url)
    soup = BeautifulSoup(markup, 'html.parser')
    if soup.select('form[action*="validateCaptcha"], input#captchacharacters'):
        return dict(status='requires_user_input', reviews=[], displayed_total=None, stop_reason='captcha')
    rows = []
    if platform == 'amazon':
        for node in soup.select('[data-hook="review"]'):
            def value(selector):
                x = node.select_one(selector)
                return x.get_text(' ', strip=True) if x else ''
            rid = node.get('id', '')
            date_text = value('[data-hook="review-date"]')
            date = ''
            match = re.search(r'on (\w+ \d{1,2}, \d{4})$', date_text)
            if match:
                try: date = dt.datetime.strptime(match[1], '%B %d, %Y').date().isoformat()
                except ValueError: pass
            rating = re.search(r'([1-5])(?:\.0)? out of 5', value('[data-hook="review-star-rating"], [data-hook="cmps-review-star-rating"]'))
            rows.append(dict(source_url=url, source_product_id=pid, review_id=rid,
                review_url=f'https://www.amazon.com/gp/customer-reviews/{rid}' if rid else '',
                title=value('[data-hook="review-title"]'), body=value('[data-hook="review-body"]'),
                author=value('.a-profile-name'), rating=int(rating[1]) if rating else None,
                original_date_text=date_text, date=date,
                verified_purchase=bool(node.select_one('[data-hook="avp-badge"]')),
                incentivized=value('[data-hook="vine-review-badge"]'),
                images=[dict(url=im.get('src',''),review_id=rid,status='needs_access_check',evidence='review container '+rid) for im in node.select('img[data-hook="review-image-tile"]')]))
    elif platform == 'wayfair':
        # Only explicit Review JSON-LD; no product image or aggregateRating conversion.
        def walk(obj):
            if isinstance(obj,list):
                for x in obj: yield from walk(x)
            elif isinstance(obj,dict):
                if obj.get('@type') == 'Review': yield obj
                else:
                    for x in obj.values(): yield from walk(x)
        for script in soup.select('script[type="application/ld+json"]'):
            try: objects=list(walk(json.loads(script.string or '')))
            except (ValueError,TypeError): continue
            for obj in objects:
                author=obj.get('author',{}); rating=obj.get('reviewRating',{})
                rows.append(dict(source_url=url,review_id=obj.get('@id',''),review_url=obj.get('url',''),body=obj.get('reviewBody',''),title=obj.get('name',''),author=author.get('name','') if isinstance(author,dict) else author,rating=rating.get('ratingValue') if isinstance(rating,dict) else None,date=obj.get('datePublished',''),original_date_text=obj.get('datePublished',''),images=[]))
    return dict(status='partial' if rows else ('unsupported' if platform=='unknown' else 'requires_user_input'), reviews=rows, displayed_total=None, collected=len(rows), stop_reason='saved_page_only_no_pagination' if rows else 'no_review_containers_or_explicit_review_schema')

if __name__ == '__main__':
    import argparse, pathlib
    p=argparse.ArgumentParser();p.add_argument('--url',required=True);p.add_argument('--html',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    result=parse_page(a.url,pathlib.Path(a.html).read_text())
    output=pathlib.Path(a.out);output.mkdir(parents=True,exist_ok=True)
    (output/'reviews.json').write_text(json.dumps(result.pop('reviews'),ensure_ascii=False,indent=2))
    (output/'collection.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result))
