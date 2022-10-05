'''
main website https://www.pexels.com
how to download pictures in pexels
'''
#-*- coding:utf-8 -*-
# patch
from gevent import monkey,pool
monkey.patch_all()

import requests, re,gevent

# 定义协程数量 ，取决于你的计算资源
thrds = pool.Pool(4)
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
response =requests.get(weburl, headers=chrome_header,allow_redirects=True)

re_file = re.findall(r'"download_link":"(.*?)"' ,str(response.text))

# download file
def download_pic(fileurl):
    if '.jpeg' in fileurl:
        # get filename
        download_link = fileurl.split('?')[0]
        with open(get_image_name(download_link),'ab+') as files:
            res = requests.get(download_link,headers=chrome_header)
            files.write(res.content)
# gevent
task_list = []

for weburl in re_file:
    task = thrds.spawn(download_pic,weburl)
    task_list.append(task)


gevent.joinall(task_list)


# 利用阿里云盘cli客户端上传
import os
filepath = os.getcwd()
for file in os.listdir(filepath):
    print(file)
    if '.jpeg' in file:
        try:
            # system级别调用cmd
            os.system('/home/ubuntu/aliyunpan-v0.2.2-linux-amd64/aliyunpan login XXXXXXXXX')
            os.system('/home/ubuntu/aliyunpan-v0.2.2-linux-amd64/aliyunpan upload %s /Public_share' % (file))
        except Exception as e:
            print(e)

