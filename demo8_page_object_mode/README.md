# python-selenium-demo


## demo 8： 使用PageObject设计模式组织用例

- page_object.py ： 存放页面元素对象及对应操作方法

```python
        self.search_box =(By.ID,'kw')
        self.search_button = (By.ID,'su')
        self.search_result = (By.XPATH,'//*[@id="1"]/h3/a[1]/em')
```

- test_run_as_page_object.py： 调用方式如下
```python
        self.driver.find_element(*testBaiduPage().search_box).send_keys('testerhome')
        self.driver.find_element(*testBaiduPage().search_button).click()
        assert 'TesterHome' in self.driver.find_element(*testBaiduPage().search_result).text
```
