import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='package')
def homepage_driver(driver):
    driver.get('https://fanyi.baidu.com/')
    for i in range(5):
        try:
            driver.find_element(by=By.XPATH,value="//span[@class='app-guide-close']").click()
            time.sleep(1)
            break
        except Exception as e:
            print(e)
            time.sleep(1)
    yield driver

