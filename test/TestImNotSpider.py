import unittest

from ImNotSpider import ImNotSpider


class TestImNotSpider(unittest.TestCase):
    def test_all(self):
        ins = ImNotSpider()
        funcs = dir(ins)
        for func in funcs:
            if func.startswith('__'):
                pass
            else:
                ua = getattr(ins, func)()
                print(ua)
                self.assertTrue(len(ua) > 0)
