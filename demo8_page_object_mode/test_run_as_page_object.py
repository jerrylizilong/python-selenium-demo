from demo8_page_object_mode.page_object import testBaiduPage
import unittest,time
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(testBaiduPage().url)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test1_testerhome(self):
        self.driver.find_element(*testBaiduPage().search_box).send_keys('testerhome')
        self.driver.find_element(*testBaiduPage().search_button).click()
        assert 'TesterHome' in self.driver.find_element(*testBaiduPage().search_result).text



if __name__ == '__main__':
    unittest.main()
