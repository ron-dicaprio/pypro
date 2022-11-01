#-*- coding:utf-8 -*-
#!/usr/bin/env python
import requests
import easygui
import json
import re
import sys
choice = easygui.choicebox(title='python小工具合集V1.0', msg='请选择对应的功能', choices=['IP地址查询工具', '手机号码查询工具'])
if choice == 'IP地址查询工具':
    ipaddr = easygui.enterbox(title='IP地址查询工具', msg='请输入IP地址')
    ipaddr = str(ipaddr)
    # IP地址正则匹配
    pat = re.compile(r'(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])')
    if pat.match(ipaddr):
        url = 'https://ipaddquery.api.bdymkt.com/ip/query'
        params = {}
        params['ip'] = ipaddr
        headers = {   
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Bce-Signature': 'AppCode/1a43f1508850485482859d3624906acf'
        }
        # 请求接口
        try:
            res = requests.request("POST", url, params=params, headers=headers)
            # json格式化
            dic = json.loads(res.content)
            if dic["code"] == 200:
                easygui.msgbox(title='IP地址查询工具', msg='IP地址查询结果如下：\n%s' % (dic['data']), ok_button='确认')
            else:
                easygui.msgbox(title='IP地址查询工具', msg='接口异常，请确认！', ok_button='确认')

        except Exception as e:
            print(e)
            easygui.msgbox(title='IP地址查询工具', msg='网络故障，请确认！', ok_button='确认')
            sys.exit(-1)

    else:
        easygui.msgbox(title='IP地址查询工具', msg='IP地址输入错误，请确认！', ok_button='确认')

if choice == '手机号码查询工具':
    #print(2)
    mobile = easygui.enterbox(title='手机号码查询工具', msg='请输入手机号码')
    mobile = str(mobile)
    pat = re.compile(r'1[34789]\d{9}')
    if pat.match(mobile):
        url = 'https://hcapi02.api.bdymkt.com/mobile'
        params = {}
        params['mobile'] = mobile
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Bce-Signature': 'AppCode/1a43f1508850485482859d3624906acf'
        }
        try:
            res = requests.request("GET", url, params=params, headers=headers)
            dic = json.loads(res.content)
            if dic["code"] == 200:
                easygui.msgbox(title='手机号码查询工具', msg='手机号码查询结果如下：\n%s' % (dic['data']), ok_button='确认')
            else:
                easygui.msgbox(title='手机号码查询工具', msg='接口异常，请确认！', ok_button='确认')
        except Exception as E:
            print(E)
            easygui.msgbox(title='手机号码查询工具', msg='网络错误，请确认！', ok_button='确认')
            sys.exit(-1)
                
        
    else:
        easygui.msgbox(title='手机号码查询工具', msg='手机号码输入错误，请确认！', ok_button='确认')
        
