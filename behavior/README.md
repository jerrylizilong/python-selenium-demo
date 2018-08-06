# 使用 behave 模块进行 BDD 行为驱动测试

## 安装：
安装 behave 模块：
```python
pip install behave
```

## 步骤定义
steps/demo.py :
该文件下定义了不同步骤：
```python
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
```

## 场景定义

### 模式1 ： 不同的测试场景（scenario）对应多个测试用例：

```python
Feature: test for the lower-upper convent
  Scenario: convent lower to upper
    When I open page
    When I input "abcdefghijk"
    When I click "大写"
    Then I see "ABCDEFGHIJK"

  Scenario: convent upper to lower
    When I open page
    When I input "ABCDEFGHIJK"
    When I click "小写"
    Then I see "abcdefghijk"

  Scenario: convent upper to lower
    When I open page
    When I input "ABCDEFghijk123"
    When I click "小写"
    Then I see "abcdefGHIJK123"
```

### 模式2： 使用数据表格，测试多组不同输入、输出
注意需要在scenario 说明： outline
```python

Feature: test for the lower-upper convent
  Scenario Outline: convent lower to upper
        When I open page
        When I input "<input_value>"
        When I click "<convent_type>"
        Then I see "<convent_result>"

     Examples: all request type
        |input_value|convent_type|convent_result|
        |abcdefghijklmn|大写|ABCDEFGHIJKLMN|
        |ABCDEFGHIJKLMN|小写|abcdefghijklmn|
        |ABCDEFGHIJKLMN|大写|ABCDEFGHIJKLMN|
        |abcdefghijklmn|大写|ABCDEFGHIJKLMn|
        |ABCDEFGHIJKLMN|小写|abcdefghijklmN|
        |ABCDEFGHIJKLMN|大写|ABCDEFGHIJKLMn|
```

## 执行： 在当前目录执行命令：

### 1. 执行目录下所有 feature 文件中的用例。
 ```python
behave  >result_all.txt

```

### 2. 执行目录下单个 feature 文件中的用例。
 ```python
behave demo.feature >result.txt


```

## 结果查看：

```python
Feature: test for the lower-upper convent # demo.feature:1

  Scenario: convent lower to upper  # demo.feature:2
    When I open page                # steps/demo.py:6
    When I input "abcdefghijk"      # steps/demo.py:13
    When I click "大写"               # steps/demo.py:18
    Then I see "ABCDEFGHIJK"        # steps/demo.py:27

  Scenario: convent upper to lower  # demo.feature:8
    When I open page                # steps/demo.py:6
    When I input "ABCDEFGHIJK"      # steps/demo.py:13
    When I click "小写"               # steps/demo.py:18
    Then I see "abcdefghijk"        # steps/demo.py:27

  Scenario: convent upper to lower  # demo.feature:14
    When I open page                # steps/demo.py:6
    When I input "ABCDEFghijk123"   # steps/demo.py:13
    When I click "小写"               # steps/demo.py:18
    Then I see "abcdefGHIJK123"     # steps/demo.py:27
      Traceback (most recent call last):
        File "c:\users\jerry\pycharmprojects\testdemo\venv\lib\site-packages\behave\model.py", line 1329, in run
          match.run(runner.context)
        File "c:\users\jerry\pycharmprojects\testdemo\venv\lib\site-packages\behave\matchers.py", line 98, in run
          self.func(context, *args, **kwargs)
        File "steps\demo.py", line 32, in assert_result
          assert value==text
      AssertionError



Failing scenarios:
  demo.feature:14  convent upper to lower

0 features passed, 1 failed, 0 skipped
2 scenarios passed, 1 failed, 0 skipped
11 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m34.963s


```
