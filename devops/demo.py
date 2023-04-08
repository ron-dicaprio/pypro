#-*- coding:utf-8 -*-
#!/usr/bin/env python3
# 脚本任何报错都会退出，请确认并核实。
'''
# 导入PyWebIO
import pywebio

# 定义一个输入文本框
input_box = pywebio.input('请输入文本：')

# 定义一个按钮
submit_btn = pywebio.button('提交')

# 定义一个文本输出框
text_output = pywebio.output('输出文本：')

# 定义一个函数，当按钮提交时调用
def submit_handler():
    text_output.value = input_box.value

# 给按钮绑定事件
submit_btn.onclick(submit_handler)

# 展示结果
pywebio.run_app(input_box, submit_btn, text_output)

import redis,sys
from os import system
# 持久化redis pool
try:
    pool = redis.ConnectionPool(host='52.69.93.175', port=35379, decode_responses=True, db=0)
    rds = redis.Redis(connection_pool=pool)
except Exception as e:
    print('redis初始化失败!',e)
    sys.exit(-1)
print(rds.get('docker-tomcat'))
'''