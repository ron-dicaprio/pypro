#-*- coding:utf-8 -*-
# patch
from gevent import monkey
monkey.patch_all()
import requests, re,gevent, multiprocessing,os

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

task_list=[]
def get_task_list():
    for weburl in re_file:
        #print(weburl)
        task_list.append(gevent.spawn(download_pic,weburl))
    return task_list

#使用协程来执行
def process_start(task_list:list):
    gevent.joinall(get_task_list())

def main():
    proc_count = 0
    # 判断协程数是否大于十万
    if len(get_task_list()) > 100000:
        # start multiprocessing
        proc = multiprocessing.Process(target=process_start,args=(task_list,))
        proc.start()
        proc.join()
        # 打印进程id
        print(os.getppid())
        proc_count+=1
        # 删掉已执行完的协程
        del task_list[0:100000]
        # 判断下是否会超过CPU核数,超过就直接用一个进程执行完
        if proc_count > os.cpu_count()-1:
            proc = multiprocessing.Process(target=process_start,args=(task_list,))
            proc.start()
            proc.join()
            # 打印进程id
            # print(os.getppid())
        else:
            pass
    else:
        proc = multiprocessing.Process(target=process_start,args=(task_list,))
        proc.start()
        proc.join()
        # 打印进程id
        # print(os.getppid())
        proc_count+=1

# 开关
if __name__ == '__main__':
    main()
