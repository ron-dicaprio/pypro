# -*- coding:utf-8 -*-
# /usr/bin/env python
import easygui as gui
import itchat
# 生成PKL文件保持登陆状态
itchat.auto_login(hotReload=True)
#itchat.auto_login(enableCmdQR=2)
#itchat.auto_login()
#itchat.send('Hello, filehelper', toUserName='filehelper')
# only use nickname to search userguid, but wechat call it username. LOL!
cmd = gui.multenterbox(msg='请输入内容和微信ID', title='微信文字助手', fields=['msg','toUser'])
print((cmd[0],cmd[1]))
user = itchat.search_friends(cmd[1])
userguid = user[0]['UserName']
# send msg to tu_user
itchat.send(cmd[0],toUserName=userguid)
