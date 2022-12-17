import allure
import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize('keyword,language,result',[
    ('test','英语','测验'),
    ('android','英语','安卓'),
    ('mobile','英语','可移动的'),
    ('country','英语','国'),
    ('value','英语','价值'),
    ('football','英语','足球运动'),
    ('篮球','中文(简体)','Basketball'),
    ('Futebol','葡萄牙语','足球运动'),
    ('ワールドカップ','日语','世界杯'),
    ('网球','中文(简体)','Tennis'),
    ('Copa del mundo','西班牙语','世界杯'),
    ('足球','中文(简体)','Football'),

])
def test_baidu_translate(homepage_driver,keyword,language,result):
    homepage_driver.find_element(by=By.ID, value='baidu_translate_input').clear()
    time.sleep(1)
    homepage_driver.find_element(by=By.ID, value='baidu_translate_input').send_keys(keyword)
    time.sleep(1)
    actual_language =  homepage_driver.find_element(by=By.XPATH,value="//span[@class='language-selected']/span").text
    actual_result = homepage_driver.find_element(by=By.XPATH,value="//p[contains(@class,'target-output')]/span").text

    filename = ("%s-%s-%s.png" %(keyword,language,result)).strip()
    homepage_driver.save_screenshot(filename)
    allure.attach.file(filename,name=filename)
    assert actual_result == result
    assert actual_language == language

