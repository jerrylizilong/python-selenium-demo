from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class steps(object):
    # 定位元素
    def find_element(self,driver,by=By.ID,value=None):
        if by in 'css selector':
            by = By.CSS_SELECTOR
        elif by in 'text':
            by = By.PARTIAL_LINK_TEXT
        elif by in 'class':
            by= By.CLASS_NAME
        elements = []
        run_time = 3
        while run_time:
            try:
                elements = driver.find_elements(by=by, value=value)
                run_time = 1
                break
            except NoSuchElementException as e:
                print(e)
            finally:
                run_time += -1
                time.sleep(2)
        if len(elements):
            return elements[0]
        print('element not found! by :%s, value :%s' %(by,value))
        return None

    # 驱动初始化
    def init_driver(self,browser_type):
        if browser_type == 'Chrome':
            driver = webdriver.Chrome()
        else:
            driver=webdriver.Firefox()
        driver.maximize_window()
        return driver

    # 前往对应 url
    def get(self,driver,para_list):
        url= para_list[0]
        driver.get(url)

    # 点击给定元素
    def click(self,driver,para_list):
        [ by, value] = para_list
        time.sleep(2)
        element = self.find_element(driver,by,value)
        if element !=None:
            element.click()

    # 在给定元素中输入对应值
    def fill(self,driver,para_list):
        [by, value,text] = para_list
        time.sleep(2)
        element = self.find_element(driver,by,value)
        if element !=None:
            element.send_keys('')
            element.send_keys(text)

    # 验证给定元素中是否包含指定文字
    def assert_text(self,driver,para_list):
        [by, value,text] = para_list
        time.sleep(2)
        element = self.find_element(driver,by,value)
        if element !=None:
            print('期待值： %s, 实际值 : %s' %(text,element.text))
            assert text in element.text

    # 验证页面标题中是否包含指定文字
    def assert_title(self,driver,para_list):
        [text] = para_list
        time.sleep(2)
        print('期待值： %s, 实际值 : %s' % (text, driver.title))
        assert text in driver.title