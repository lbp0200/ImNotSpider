import unittest

from ImNotSpider import ImNotSpider


class TestWap(unittest.TestCase):
    def test_wechat(self):
        ins = ImNotSpider()
        ua = ins.wechat_iphone()
        print(ua)
        self.assertTrue(len(ua) > 0)

    def test_uc(self):
        ins = ImNotSpider()
        ua = ins.uc_browser()
        print(ua)
        self.assertTrue(len(ua) > 0)

    def test_baidu_browser(self):
        ins = ImNotSpider()
        ua = ins.baidu_box_app()
        print(ua)
        self.assertTrue(len(ua) > 0)


if __name__ == '__main__':
    unittest.main()
