import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from sources import parse_page
class SourceTest(unittest.TestCase):
    def test_review_images_scoped(self):
        page='''<img src="product.jpg"><div data-hook="review" id="synthetic"><span data-hook="review-body">合成评论</span><span data-hook="review-star-rating">2.0 out of 5 stars</span><img data-hook="review-image-tile" src="buyer.jpg"></div>'''
        r=parse_page('https://www.amazon.com/dp/B00006IEEU',page)
        self.assertEqual(r['status'],'partial')
        self.assertEqual([x['url'] for x in r['reviews'][0]['images']],['buyer.jpg'])
    def test_captcha_and_unknown(self):
        self.assertEqual(parse_page('https://www.amazon.com/dp/B00006IEEU','<input id="captchacharacters">')['status'],'requires_user_input')
        self.assertEqual(parse_page('https://example.org','')['status'],'unsupported')
    def test_wayfair_aggregate_not_review(self):
        self.assertFalse(parse_page('https://www.wayfair.com/test','<script type="application/ld+json">{"@type":"Product","image":"product.jpg","aggregateRating":{"ratingValue":5}}</script>')['reviews'])
