# python-selenium-demo

## demo 7： 使用独立的用例文件管理用例

### 用例步骤、关键字定义： 与 demo6 相同。

### 用例执行：
- 用例可以使用不同的存储方式进行独立存储，完全脱离于执行用例的脚本。
- 可通过数据库、excel、txt 等不同的方式存储用例。 这里以txt 为例，演示如何读取用例并执行。
- 为提高测试执行效率，使用multiprocessing 模块对用例进行并发执行。 可根据需要设置具体的并发数。

### 用例文件样例：
```
Chrome,前往|http://www.baidu.com,验证标题|百度一下,填写|id@@kw@@百度,点击|id@@su,验证文字|xpath@@//*[@id="1"]/h3/a/em@@百度
Chrome,前往|http://www.baidu.com,点击|name@@tj_trnews,验证标题|百度新闻
Chrome,前往|http://www.baidu.com,点击|name@@tj_trhao123,验证标题|hao123
Chrome,前往|http://www.baidu.com,点击|name@@tj_trmap,验证标题|百度地图
Chrome,前往|http://www.baidu.com,点击|name@@tj_trtieba,验证标题|百度贴吧
```

### 用例读取与执行方法：

```python
from demo7_get_case_from_file import keywords
import os,platform
from multiprocessing.dummy import Pool as ThreadPool

# 获取文件完整路径名称
def get_filename():
    path = os.getcwd()
    if platform.system() == 'Windows':
        path =path + '/'
    else:
        path = path +'\\'
    filename = path + 'cases.txt'
    return filename

# 从 txt 中读取内容的方法， 可根据不同的存放方式进行替换， 如 存放到 excel 或者数据库，则替换为对应的读取方法
def read_case(filename):
    fr=open(filename,encoding='utf-8',mode='r')
    contents = fr.readlines()
    cases = []
    for content in contents:
        cases.append(content.strip('\n'))
    return cases

# 并发执行，传入用例队列和并发数
def multipleRun(caselist, threadNum):
    pool = ThreadPool(threadNum)
    pool.map(keywords.run, caselist)
    pool.close()
    pool.join()

def main():
    cases = read_case(get_filename())
    multipleRun(cases,3)

if __name__ == '__main__':
    main()

```