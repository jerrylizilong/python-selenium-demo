# python-selenium-demo

## demo 6： 使用关键字驱动模式组织用例


### keyword: 
- 以关键字的方式组织用例步骤，可以将用例从脚本中脱离。
- keywords.py 文件中定义了不同关键字对应的执行方法
```python
from data_driven.steps import steps

# 关键字定义，通过关键字匹配对应的方法。 可根据需要新增对应的关键字和对应方法。
def get_keyword(driver,keyword,para_list):
    if keyword in ['Chrome','Firefox']:
        return steps().init_driver(keyword)
    elif keyword=='前往':
        return steps().get(driver,para_list)
    elif keyword=='填写':
        return steps().fill(driver,para_list)
    elif keyword=='点击':
        return steps().click(driver,para_list)
    elif keyword=='验证文字':
        return steps().assert_text(driver,para_list)
    elif keyword=='验证标题':
        return steps().assert_title(driver,para_list)

# 执行方法，逐个步骤转换为对应的关键字方法，并执行
def run(case):
    step_list = case.split(',')
    driver = get_keyword('',step_list[0],[])
    step_list.remove(step_list[0])
    for step in step_list:
        keyword, para_list = step.split('|')[0],step.split('|')[1].split('@@')
        get_keyword(driver,keyword,para_list)
    driver.get_screenshot_as_png()
    driver.quit()


```

- 用例样例：
```python
Chrome,前往|http://www.baidu.com,验证标题|百度一下,填写|id@@kw@@百度,点击|id@@su,验证文字|xpath@@//*[@id="1"]/h3/a/em@@百度
```
- 关键字格式：
```python
关键字|元素定位方式@@元素属性值@@其他参数。 
如： 填写|id@@kw@@百度   表示步骤为“填写”， 通过 id = kw 定位元素，并在定位元素中输入 “百度”
```

### 步骤定义：
- steps.py 文件中定义了关键字对应的执行方法：

```python
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
            element.send_keys()
            element.send_keys(text)

    # 验证给定元素中是否包含指定文字
    def assert_text(self,driver,para_list):
        [by, value,text] = para_list
        time.sleep(2)
        element = self.find_element(driver,by,value)
        if element !=None:
            print(text,element.text)
            assert text in element.text

    # 验证页面标题中是否包含指定文字
    def assert_title(self,driver,para_list):
        [text] = para_list
        time.sleep(2)
        print(text,driver.title)
        assert text in driver.title

```

### 用例执行：
- test_run_as_data_driven.py 文件中给出了5条对应的例子，分别对百度首页五个链接和功能进行测试。

```python

from data_driven import keywords
import unittest


class MyTestCase(unittest.TestCase):

    def test1_baidu_search(self):
        case0 = 'Chrome,前往|http://www.baidu.com,验证标题|百度一下,填写|id@@kw@@百度,点击|id@@su,验证文字|xpath@@//*[@id="1"]/h3/a/em@@百度'
        keywords.run(case0)

    def test1_news(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trnews,验证标题|百度新闻'
        keywords.run(case0)

    def test1_hao123(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trhao123,验证标题|hao123'
        keywords.run(case0)

    def test1_map(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trmap,验证标题|百度地图'
        keywords.run(case0)

    def test1_tieba(self):
        case0 = 'Chrome,前往|http://www.baidu.com,点击|name@@tj_trtieba,验证标题|百度贴吧'
        keywords.run(case0)


if __name__ == '__main__':
    unittest.main()

```