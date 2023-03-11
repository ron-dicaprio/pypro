#-*- coding:utf-8 -*-
#!/usr/bin/env python

# Time Part
import time
def GetCurrDay():
    return time.strftime("%Y-%m-%d")

def GetCurrTime():
    return time.strftime("%Y-%m-%d %H:%M:%S")

# requests Part
import requests,json
def dingtalk(contenct,keyword):
    token='token'
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (token)
    chorme_header  = {"Content-Type": "application/json","Charset": "UTF-8"}
    contenct = keyword + ':' + contenct
    message = {
        "msgtype": "text",
        "text": {
            "content": contenct
        },
        "at": {
            #是否@所有人，Ture or False
            "isAtAll": False
        }
    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    print('json格式为：',message_json)
    # 发送请求
    try:
        info = requests.post(url=webhook, data=message_json, headers=chorme_header)
        # 打印返回的结果
        print('消息发送成功!返回信息为：', info.text)
    except Exception as e:
        print(e)


# 心灵鸡汤日语
def daily_words():
    chrome_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    weburl='https://api.xwteam.cn/api/soup/lucky'
    keydata={
		'key': '0vXEDJ1E9L4Bd6u9VSkR3BZ7wx',
        'type': '1'
	}
    try:
        resp = requests.post(weburl,headers=chrome_header,data=keydata).content
        result=json.loads(resp)
        for value in result['data'].values():
            return value
    except Exception as e:
        return e


# File IO Part

# pymysql engine to run sql command.
import configparser,pymysql
def exec_pymysql(str_sql):
    try:
        config = configparser.ConfigParser() 
        # 配置文件带中文字符，必须定义编码方式
        config.read("etc/dockerdb.ini",encoding='utf-8')
        key_host=config.get("dockerhost", "host") 
        key_port=config.getint("dockerhost", "port") 
        key_user=config.get("dockerhost", "dbuser")
        key_passwd=config.get("dockerhost", "dbpasswd")
        key_db=config.get("dockerhost", "db")
        conn = pymysql.connect(host=key_host,port=key_port,user=key_user, passwd=key_passwd, db=key_db,charset='utf8mb4')
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()
        conn.close()
        return cur.fetchall()
    except Exception as ERRORS:
        return ERRORS






# Random
import random,string
def get_active_code(Lenth,Nums):
    active_code_list=[]
    # 取值的池子
    code_pool = "0123456789" + string.ascii_uppercase     
    for codes in range(0,Nums):
        # 定义取值长度
        # choices:放回抽样,sample:不放回抽样
        # active_code = ''.join(random.choices(code_pool,k=Lenth))
        active_code = ''.join(random.sample(code_pool,Lenth))
        if active_code in active_code_list:
            # 如果有重复的会导致生成出来active_code_list的数量少一位. 
            # todo list
            pass
        else:
            active_code_list.append(active_code)
    return active_code_list

# Moviepy
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
# 合并文件夹里面的所有文件,需要确保所有文件都是视频文件
def py_combfloderAV(self):
    video_list = []
    #将文件路径写到list里面
    for file in os.listdir(self):
        videos_dir = self + file
        video_list.append(videos_dir)
    #定义一个空字典
    clip = {}
    for n in range(0,len(video_list)):
        clip[n] = VideoFileClip(video_list[n])
        # 当文件较大时, 内存可能溢出, 待优化
        finalclip = concatenate_videoclips([clip[h] for h in range(0, len(video_list))])
        finalclip.write_videofile(self + "combine_%s.mp4" % (time.strftime('%Y%m%d%H%M%S')))


import gevent
# secret-key should in headers
chrome_header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'secret-key':'H2jk9uKnhRmL6WPwh89zBezWvr'
    }
# Get Filename Which Endwith Pictre Format
import re
def get_image_from_files(url):
    pattern = re.search("([|.|\w|\s|-])*?.(jpg|png|jpeg|bmp)", url.lower())
    if not pattern:
        return False
    else:
        return True
# get filename from url address.
def get_image_name(url):
    pattern = re.search("([|.|\w|\s|-])*?.(jpg|gif|png|jpeg)", url)
    if not pattern:
        return None
    image_name = pattern.group()
    return image_name
# download file
def download_pic(fileurl):
    if '.jpeg' in fileurl:
        # get filename
        download_link = fileurl.split('?')[0]
        with open(get_image_name(download_link),'ab+') as files:
            res = requests.get(download_link,headers=chrome_header)
            files.write(res.content)

re_file=[]
task_list=[]
def get_task_list():
    for weburl in re_file:
        #print(weburl)
        task_list.append(gevent.spawn(download_pic,weburl))
    return task_list

#使用协程来执行
def main(task_list:list):
    gevent.joinall(get_task_list())