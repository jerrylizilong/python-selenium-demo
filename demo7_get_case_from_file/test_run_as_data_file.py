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