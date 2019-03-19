from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testBaiduPage(object):
    def __init__(self):
        # 定义搜索框、 搜索结果的定位条件和值
        self.url ='http://www.baidu.com'
        self.search_box =(By.ID,'kw')
        self.search_button = (By.ID,'su')
        self.search_result = (By.XPATH,'//*[@id="1"]/h3/a[1]/em')


