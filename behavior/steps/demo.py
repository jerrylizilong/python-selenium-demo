from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *

@when(u'I open page')
def open(context):
# 初始化，打开浏览器，输入网址，并最大化
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get('http://www.bejson.com/convert/uplowercase/')

@when(u'I input "{text}"')
def input(context,text):
    # 输入搜索字符串
    context.browser.find_element(by='id' ,value='content').send_keys(text)

@when(u'I click "{text}"')
def click_by_text(context,text):
    # 点击转换大写、小写
    if '大写' in text:
        context.browser.find_element(by=By.XPATH
                            ,value='/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/button[1]').click()
    else:
        context.browser.find_element(by=By.XPATH
                                     , value='/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/button[2]').click()

@then(u'I see "{text}"')
def assert_result(context,text):
    # 等待2秒后，获取转换结果，并退出浏览器
    time.sleep(2)
    value=context.browser.find_element(by='id', value='result').get_attribute('value')
    assert value==text
    context.browser.quit()