from selenium import webdriver
import time

# 初始化，打开浏览器，输入网址，并最大化
driver = webdriver.Chrome()
driver.get('http://www.bejson.com/convert/uplowercase/')
driver.maximize_window()

# 输入搜索字符串、点击转换大写
driver.find_element(by='id' ,value='content').send_keys('abcde')
driver.find_element(by='css selector'
                        ,value='body > div.aw-container-wrap > div > div > div > div > div.panel.panel-default > div.panel-body > div.btn-group > button:nth-child(1)').click()

# 等待2秒后，获取转换结果，并退出浏览器
time.sleep(2)
result = driver.find_element(by='id', value='result').get_attribute('value')
print(result)
driver.quit()