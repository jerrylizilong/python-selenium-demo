# python-selenium-demo

## 1.demo1： 使用 python + selenium 调用浏览器进行操作的例子。

demo.py :

 执行该文件，完成第一个目标：实现自动打开网页、输入待转换数据、点击转换按钮、获取转换结果的过程。


## 2.unittest_version： 使用unittest 实现多个用例调用的例子，并进行断言判断。
convert_up_low_test.py: 
  实现第二个目标：使用unittest ，对不同的输入数据进行测试和验证结果。

## 3.pytest_version： 使用pytest执行目录中所有test 文件，并生成对应 html 报告文件。
###  3.1 pytest
使用 pytest 执行测试用例，并生成对应的 html report。

### 3.2 所需模块
- 安装pytest： pip install pytest
- 安装pytest-html: pip install pytest-html

### 3.3 demo
执行 run_pytest.bat 文件，将查找当前目录中 test 开头的py 文件，并执行其中的 test 方法，最终生成 html 格式的报告。

### 3.4报告样例（在浏览器中打开）： 

test_report_20180805-233950.html