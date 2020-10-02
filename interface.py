# -*- coding:utf-8 -*-
# !usr/bin/env python
#一个超级简单的post请求接口
import time
import flask
interface = flask.Flask(__name__)
@interface.route('/index',methods = ['post'])
def webservice():
    username = flask.request.json.get('username')
    print(username)
    passwd = flask.request.json.get('password')
    print(passwd)
    return('{%s,%s}'% (username,passwd))
if __name__ == "__main__":
    interface.run(port = 9000,debug=True,host = '127.0.0.1')
