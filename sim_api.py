#-*- coding:utf-8 -*-
#!/usr/bin/env python
import requests,json
# 心灵鸡汤日语
def daily_words():
    chrome_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    #weburl='https://api.xwteam.cn/api/soup/lucky?key=0vXEDJ1E9L4Bd6u9VSkR3BZ7wx&type=1'
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

# 获取域名ICP信息
def get_domain_info(doamin):
    chrome_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    weburl='https://api.xwteam.cn/api/domain/icp'
    keydata={
		'key': '0vXEDJ1E9L4Bd6u9VSkR3BZ7wx',
        'url': doamin
	}    
    try:
        resp = requests.post(weburl,headers=chrome_header,data=keydata).content
        result=json.loads(resp)
        return result['data']
    except Exception as e:
        return e    


# 获取天气信息
def get_weather(province,city):
    chrome_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    weburl='https://api.xwteam.cn/api/weather/weather'
    keydata={
		'key': '0vXEDJ1E9L4Bd6u9VSkR3BZ7wx',
        'province': province,
        'city': city
	}    
    try:
        resp = requests.post(weburl,headers=chrome_header,data=keydata).content
        result=json.loads(resp)
        return result['data']
    except Exception as e:
        return e  



# 获取抖音短视频短地址
def get_tiktokurl(tiktok_url):
    #                            Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
    chrome_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    weburl='https://api.xwteam.cn/api/analysis/douyin'
    keydata={
		'key': '0vXEDJ1E9L4Bd6u9VSkR3BZ7wx',
        'type': 'hide',
        'url': tiktok_url
	}    
    try:
        resp = requests.post(weburl,headers=chrome_header,data=keydata,allow_redirects=True).content
        result=json.loads(resp)
        return result['data']
    except Exception as e:
        return e      



tiktok_urls='https://v.douyin.com/hauaTou/'

print(get_tiktokurl(tiktok_urls)['play'])



















""" 
config.add_section("Haha")     # 创建一个组：Haha
config.set("Haha", "name", "haha")   # 给Haha组添加一个属性name=haha
config.remove_section('Xixi')   # 删除一个section
config.remove_option('LILY',"name")  # 删除一个配置项
# 写入 config.ini
# r:读，r+:读写，w:写，w+:写读，a:追加，a+:追加读写
# 写读和读写的区别：读写，文件已经存在；读写，创建新的文件
#将文件内容读取到内存中，进过一系列操作之后必须写回文件，才能生效。写回文件的方式如下：（使用configparser的write方法）
f = open('config1.ini', 'w')
config.write(f)
f.close() 

# pymysql engine to run sql command.
import pymysql,configparser
def mysql_dbconn(self):
    # 实例化ConfigParser
    try:    
        config = configparser.ConfigParser() 
        config.read("dbconf.cfg")
        #print(config.sections())
        key_host=config.get("dockerhost", "host") 
        key_port=config.getint("dockerhost", "port") 
        key_user=config.get("dockerhost", "dbuser")
        key_passwd=config.get("dockerhost", "dbpasswd")
        key_db=config.get("dockerhost", "db")
        conn = pymysql.connect(host=key_host,port=key_port,user=key_user, passwd=key_passwd, db=key_db,charset='utf8mb4')
        cur = conn.cursor()
        cur.execute(self)
        conn.commit()
        conn.close()
        #print('sql execute succsess!')
        return cur.fetchall()
    except Exception as ERROR:
        return ERROR

print(pyrunsql('show tables;'))


#dbconfig
[dockerhost]
host=172.31.65.168
port=3306
dbuser=root
dbpasswd=@Caitao628422
db=epointoneapm


[db_name]
name='zhangsan'


"""