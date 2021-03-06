from selenium import webdriver
import time
import os

class convert_md5():
    def __init__(self):
        self.path = os.getcwd()

    def md5(self, keyword):
        driver = webdriver.Chrome()
        driver.get('http://www.bejson.com/enc/md5/')
        driver.maximize_window()

        driver.find_element(by='id',value='str').send_keys(keyword)
        driver.find_element(by='css selector',value='body > div.aw-container-wrap > div > div > div > div > div.panel.panel-default > div.panel-body > div.btn-group > button.btn.btn-primary').click()

        time.sleep(2)
        driver.save_screenshot(self.path+'/'+str(time.time())+'.png')
        result = driver.find_element(by='id', value='estr').get_attribute('value')
        print(result)
        driver.quit()
        return result

    def md52(self, preosign):
        import hashlib
        m = hashlib.md5()
        preosign = preosign.encode('utf-8')
        m.update(preosign)
        print(m.hexdigest())
        return m.hexdigest()