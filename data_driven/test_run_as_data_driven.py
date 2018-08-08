from data_driven import keywords
import unittest


class MyTestCase(unittest.TestCase):

    def test1_baidu_search(self):
        case0 = 'Chrome,前往|http://www.baidu.com,验证标题|百度一下,填写|id@@kw@@百度,点击|id@@su,验证文字|xpath@@//*[@id="1"]/h3/a/em@@百度'
        keywords.run(case0)

    def test1_news(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trnews,验证标题|百度新闻'
        keywords.run(case0)

    def test1_hao123(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trhao123,验证标题|hao123'
        keywords.run(case0)

    def test1_map(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trmap,验证标题|百度地图'
        keywords.run(case0)

    def test1_tieba(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trtieba,验证标题|百度贴吧'
        keywords.run(case0)


if __name__ == '__main__':
    unittest.main()
