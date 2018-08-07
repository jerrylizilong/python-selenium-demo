from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testBaiduPage(object):
    def __init__(self):
        # 定义搜索框、 搜索结果的定位条件和值
        self.search_box = [By.ID,'kw']
        self.search_result = [By.XPATH,'//*[@id="1"]/h3/a[1]/em']

    def init_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.baidu.com')
        return driver

    def search(self,keyword):
        # 初始化
        driver = self.init_driver()
        # 输入关键词
        driver.find_element(by=self.search_box[0],value=self.search_box[1]).send_keys(keyword)
        time.sleep(2)
        # 输入回车进行查找， 可替换为点击  百度一下  按钮
        driver.find_element(by=self.search_box[0], value=self.search_box[1]).send_keys('\n')
        time.sleep(2)
        # 获取第一条结果的文字
        result = driver.find_element(by=self.search_result[0],value=self.search_result[1]).text
        # 验证结果是否符合预期
        print('keyword: %s,  result : %s' %(keyword,result))
        assert keyword in result
        driver.quit()