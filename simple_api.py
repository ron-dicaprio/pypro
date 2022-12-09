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
