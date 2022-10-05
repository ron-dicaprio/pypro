#-*- coding:utf-8 -*-
# patch
from gevent import monkey
monkey.patch_all()
import requests, re,gevent, multiprocessing

# get filename from url address.
def get_image_name(url):
    pattern = re.search("([|.|\w|\s|-])*?.(jpg|gif|png|jpeg)", url)
    if not pattern:
        return None
    image_name = pattern.group()
    return image_name

# default weburl
weburl ='https://www.pexels.com/zh-cn/api/v2/feed?seed=2022-10-03T14:39:12.839Z&per_page=8'

# secret-key should in headers
chrome_header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'secret-key':'H2jk9uKnhRmL6WPwh89zBezWvr'
    }

# allow_redirects允许跳转
response =requests.get(weburl, headers=chrome_header,allow_redirects=True,timeout=5)
# 取url值
re_file = re.findall(r'"download_link":"(.*?)"' ,str(response.text))

# download file
def download_pic(fileurl):
    if '.jpeg' in fileurl:
        # get filename
        download_link = fileurl.split('?')[0]
        with open(get_image_name(download_link),'ab+') as files:
            res = requests.get(download_link,headers=chrome_header)
            files.write(res.content)

task_list = []
#使用协程来执行
def process_start(task:list):
    for weburl in re_file:
        task_list.append(gevent.spawn(download_pic,weburl))
    gevent.joinall(task)

def main():
    proc = multiprocessing.Process(target=process_start,args=(task_list,))
    proc.start()
    proc.join()

# 记录一下进程数量
if __name__ == '__main__':
    main()


'''
# start multiprocessing.......
# 判断协程是否大于十万，大于十万则开启多线程
while task_list is not None:
    if len(task_list) > 100000:
        # start multiprocessing
        proc = multiprocessing.Process(target=process_start,args=(task_list,))
        proc.start()
        proc.join()
        # 打印进程id
        print(os.getppid())
        proc_count+=1
        # 删掉已执行完的协程
        del task_list[0:100000]
        # 判断下是否会超过CPU核数
        if proc_count > os.cpu_count()-1:
            proc = multiprocessing.Process(target=process_start,args=(task_list,))
            proc.start()
            proc.join()
            # 打印进程id
            # print(os.getppid())
    else:
        proc = multiprocessing.Process(target=process_start,args=(task_list,))
        proc.start()
        proc.join()
        # 打印进程id
        # print(os.getppid())
        proc_count+=1



#-*- coding=utf-8 -*-
import requests

from multiprocessing import Process
import gevent
from gevent import monkey; monkey.patch_all()

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def fetch(url):
    try:
        s = requests.Session()
        r = s.get(url,timeout=1)#在这里抓取页面
        r.close()#用完之后记得释放资源，不然会出现很多僵尸进程
    except Exception,e:
        print e 
    return ''

 

def process_start(tasks):
    gevent.joinall(tasks)#使用协程来执行

def task_start(filepath,flag = 100000):#每10W条url启动一个进程
    with open(filepath,'r') as reader:#从给定的文件中读取url
        url = reader.readline().strip()#通过readline每次读取一行，避免一次读取全部url导致内存不够用。
        task_list = []#这个list用于存放协程任务
        i = 0 #计数器，记录添加了多少个url到协程队列
        while url!='':
            i += 1
            task_list.append(gevent.spawn(fetch,url,queue))#每次读取出url，将任务添加到协程队列
            if i == flag:#一定数量的url就启动一个进程并执行
                p = Process(target=process_start,args=(task_list,))
                p.start()
                task_list = [] #重置协程队列
                i = 0 #重置计数器
            url = reader.readline().strip()

        if task_list not []:#若退出循环后任务队列里还有url剩余
            p = Process(target=process_start,args=(task_list,))#把剩余的url全都放到最后这个进程来执行
            p.start()
  
if __name__ == '__main__':
    task_start('./testData.txt')#读取指定文件
'''