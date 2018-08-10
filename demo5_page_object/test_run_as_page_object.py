from demo5_page_object.page_object import testBaiduPage
import unittest


class MyTestCase(unittest.TestCase):

    def test1_testerhome(self):
        testBaiduPage().search(keyword='TesterHome')

    def test_163(self):
        testBaiduPage().search(keyword='网易')

    def test_sina(self):
        testBaiduPage().search(keyword='新浪首页')

    def test_sohu(self):
        testBaiduPage().search(keyword='搜狐')

    def test_baidu(self):
        testBaiduPage().search(keyword='百度')

    def test_google(self):
        testBaiduPage().search(keyword='Google')


    def test_tencent(self):
        testBaiduPage().search(keyword='腾讯')

    def test_taobao(self):
        testBaiduPage().search(keyword='淘宝')

    def test_jd(self):
        testBaiduPage().search(keyword='京东')

    def test_meituan(self):
        testBaiduPage().search(keyword='美团')


if __name__ == '__main__':
    unittest.main()
