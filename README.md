# python-selenium-demo

## demo 1. 使用 python + selenium 调用浏览器进行操作的例子。

demo.py :

 执行该文件，完成第一个目标：实现自动打开网页、输入待转换数据、点击转换按钮、获取转换结果的过程。


## demo 2. unittest_version： 使用unittest 实现多个用例调用的例子，并进行断言判断。
convert_up_low_test.py: 
  实现第二个目标：使用unittest ，对不同的输入数据进行测试和验证结果。

## demo 3.pytest_version： 使用pytest执行目录中所有test 文件，并生成对应 html 报告文件。
###  3.1 pytest
使用 pytest 执行测试用例，并生成对应的 html report。

### 3.2 所需模块
- 安装pytest： pip install pytest
- 安装pytest-html: pip install pytest-html

### 3.3 demo
执行 run_pytest.bat 文件，将查找当前目录中 test 开头的py 文件，并执行其中的 test 方法，最终生成 html 格式的报告。

### 3.4报告样例（在浏览器中打开）： 

test_report_20180805-233950.html

## demo 4： 使用 Python behave 模块进行 BDD 行为驱动测试

behavior 模块, 样例：

```python
Feature: test for the lower-upper convent
  Scenario: convent lower to upper
    When I open page
    When I input "abcdefghijk"
    When I click "大写"
    Then I see "ABCDEFGHIJK"
```

## demo 5. 使用PageObject设计模式组织用例

- page_object.py ： 存放页面元素对象及对应操作方法

- test_run_as_page_object.py： 
10条用例，分别在百度页面搜索一个关键字，并验证查询结果第一条是否包含关键字。

## demo 6： 使用关键字驱动模式组织用例

### keyword: 
- 以关键字的方式组织用例步骤，可以将用例从脚本中脱离。
- keywords.py 文件中定义了不同关键字对应的执行方法
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
- steps.py 文件中定义了关键字对应的执行方法

### 用例执行：
- test_run_as_data_driven.py 文件中给出了5条对应的例子，分别对百度首页五个链接和功能进行测试。


## demo 7： 使用独立的用例文件管理用例

### 用例步骤、关键字定义： 与 demo6 相同。

### 用例执行：
- 用例可以使用不同的存储方式进行独立存储，完全脱离于执行用例的脚本。
- 可通过数据库、excel、txt 等不同的方式存储用例。 这里以txt 为例，演示如何读取用例并执行。
- 为提高测试执行效率，使用multiprocessing 模块对用例进行并发执行。 可根据需要设置具体的并发数。


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
