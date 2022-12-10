#-*- coding:utf-8 -*-
#!/usr/bin/env python
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）。
import random,string
def get_active_code(Lenth,Nums):
    active_code_list=[]
    for codes in range(0,Nums):
        # 取值的池子
        code_pool = "0123456789" + string.ascii_uppercase 
        # 定义长度
        active_code = ''.join(random.sample(code_pool,Lenth))
        if active_code in active_code_list:
            # 如果有重复的会导致生成出来active_code_list的数量少一位. 后期优化(while True)
            # todo list
            pass
        else:
            active_code_list.append(active_code)
    return active_code_list

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql
def exec_pymysql(str_sql):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root',db='active_codes', passwd='Gepoint',charset='utf8mb4')
        cur = conn.cursor()
        cur.execute(str_sql)
        conn.commit()
        conn.close()
        return cur.fetchall()
    except Exception as ERRORS:
        return ERRORS

#str_sql="create database active_codes charset = utf8;"
str_sql1="CREATE TABLE `active_codes_pool`  ( \
    `No` int(11) NOT NULL AUTO_INCREMENT PRIMARY key, \
    `active_code` varchar(50) NOT NULL \
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4;"
try:
    res1 = exec_pymysql(str_sql1)
    print(res1)
except Exception as e:
    print(e)

for active_codes in get_active_code(20,10):
    print(active_codes)
    str_sql2='insert into active_codes_pool (active_code) values ("%s") ' % (active_codes)
    try:
        res2 = exec_pymysql(str_sql2)
        print(res2)
    except Exception as e:
        print(e)



# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis
# 连接redis，写到序号0的缓存库中
redis_conn=redis.Redis(host='127.0.0.1',port=6379,DB=0)


# 没装redis 未验证
for redis_value in get_active_code(20,10):
    redis_conn.lpush('code',redis_value) 

# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import string,re
def get_count():
    get_count_list=dict()
    code_pool = string.ascii_uppercase 
    content=open('D:\\script-factory\\python factory\\pyfile\\aria2c.txt','r').read().upper()
    #print(content)
    for key in code_pool:
        res = re.findall(key,content)
        print(key,':',len(res))
        get_count_list.update({key:len(res)})
        print(get_count_list)
    return get_count_list


# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

