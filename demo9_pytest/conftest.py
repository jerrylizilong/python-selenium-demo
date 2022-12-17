import pytest
from selenium.webdriver.safari import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def driver(url=''):
    driver = webdriver.WebDriver()
    if len(url):
        driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()

@pytest.fixture()
def baidu_driver(driver):
    driver.get('https://www.baidu.com')
    yield driver

def test_search(baidu_driver):
    baidu_driver.find_element(by=By.ID,value='kw').send_keys('testerhome')
    baidu_driver.find_element(by=By.ID,value='su').click()
    assert baidu_driver.find_element(by=By.XPATH,value="//div[@id='content_left']//div[@id='1']//em").text == 'TesterHome'
    baidu_driver.save_screenshot('result.png')

if __name__=='__main__':
    driver()