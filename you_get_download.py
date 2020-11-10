# -*- coding: utf-8 -*-
# !usr/bin/env python
#通过python下的you_get模块来下载文件
import sys
import os
from you_get import common
chorme_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}
def you_get_download(weburl,path):
    common.any_download(url= weburl, stream_id= 'dash-flv720',output_dir = path, merge = True)
    
    

'''
import sys
from you_get import common as you_get       #导入you-get库

directory = r'D:\1'                         #设置下载目录
url = 'https://www.bilibili.com/video/av27036095/'      #需要下载的视频地址
sys.argv = ['you-get','-o',directory,url]       #sys传递参数执行下载，就像在命令行一样
you_get.main()


class Student(obiect):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s: %s" % (self.name, self.score)


#通过subprocess主进程来下载文件
import subprocess
for i in range(1,2):
    url = 'https://www.bilibili.com/video/BV187411f7z9?p=%s' % (i)
    command = 'you-get -o d:\\pydownload --format=dash-flv720 %s' % (url)
    #command = 'you-get -i %s'  % (url)
    print(subprocess.run(command, shell=True))
'''
