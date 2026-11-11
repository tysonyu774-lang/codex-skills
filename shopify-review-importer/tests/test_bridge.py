import sys, pathlib, sqlite3, unittest, tempfile, csv
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from bridge import prepare, export, identify
class BridgeTest(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:')
        self.url='https://www.amazon.com/dp/B00006IEEU'
        self.target=dict(store='test.myshopify.com',handle='test',product_id='123')
        self.c=dict(plugin='judgeme',reuse_authorized=True,target=self.target,mappings={self.url:self.target})
        self.r=dict(source_url=self.url,review_id='synthetic-1',body='合成测试,"引号"\n😀<script>alert(1)</script>',rating=2,date='2024-01-31',author='合成作者',images=[])
    def test_csv_unicode_pending(self):
        ready,issues=prepare([self.r],self.c,self.db)
        self.assertFalse(issues)
        with tempfile.TemporaryDirectory() as tmp:
            for plugin in ('judgeme','loox'):
                path=pathlib.Path(tmp)/'test.csv'; export(ready,plugin,path)
                with path.open(encoding='utf-8-sig',newline='') as f: row=next(csv.DictReader(f))
                self.assertEqual(row['body'],self.r['body'])
                if plugin=='judgeme': self.assertEqual(row['curated'],'not-yet'); self.assertEqual(row['review_date'],'31/01/2024')
    def test_guards_and_duplicate(self):
        self.assertEqual(len(prepare([self.r,self.r],self.c,self.db)[0]),1)
        for field,value in [('date',''),('rating',6),('images',[{'url':'/local.jpg'}])]:
            r=dict(self.r);r[field]=value
            self.assertFalse(prepare([r],self.c,self.db)[0])
        self.c['mappings']={};self.assertFalse(prepare([self.r],self.c,self.db)[0])
    def test_unknown_confirmed_and_changes(self):
        r=prepare([self.r],self.c,self.db)[0][0]
        for state in ('submitted','unknown','confirmed'):
            self.db.execute('INSERT OR REPLACE INTO ledger VALUES (?,?,?)',(r['ledger_key'],r['fingerprint'],state))
            self.assertFalse(prepare([self.r],self.c,self.db)[0])
        changed=dict(self.r,body='changed');self.assertIn('changed_review_requires_reconciliation',prepare([changed],self.c,self.db)[1][0]['issues'])
    def test_host(self):
        self.assertEqual(identify('https://amazon.com.evil.org/dp/B00006IEEU')[0],'unknown')
if __name__=='__main__': unittest.main()
