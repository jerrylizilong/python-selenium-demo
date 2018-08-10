from selenium import webdriver
import time
import os

class convert_up_low():
    def __init__(self):
        self.path = os.getcwd()

    def convert_up_low(self, keyword,method):
        driver = webdriver.Chrome()
        driver.get('http://www.bejson.com/convert/uplowercase/')
        driver.maximize_window()

        driver.find_element(by='id',value='content').send_keys(keyword)
        if method == 'upper':
            driver.find_element(by='css selector',
                                value='body > div.aw-container-wrap > div > div > div > div > div.panel.panel-default > div.panel-body > div.btn-group > button:nth-child(1)').click()
        else:
            driver.find_element(by='css selector',
                                value='body > div.aw-container-wrap > div > div > div > div > div.panel.panel-default > div.panel-body > div.btn-group > button:nth-child(2)').click()

        time.sleep(2)
        driver.save_screenshot(self.path+'/'+str(time.time())+'.png')
        result = driver.find_element(by='id', value='result').get_attribute('value')
        print(result)
        driver.quit()
        return result

