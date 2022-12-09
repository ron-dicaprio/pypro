#!-*- coding:utf-8 -*-
from os.path import isfile
from easygui import fileopenbox,msgbox
from hashlib import md5
def getBigFileMD5(filepath):
    if isfile(filepath):
        md5obj = md5()
        maxbuf = 8192
        f = open(filepath,'rb')
        while True:
            buf = f.read(maxbuf)
            if not buf:
                break
            md5obj.update(buf)
        f.close()
        hash = md5obj.hexdigest()
        return str(hash).upper()
    return None

cacu_md5=msgbox(title='MD5哈希值计算器', msg='请点击开始计算选择所需要计算MD5的文件！',ok_button='开始计算')
if  cacu_md5 == '开始计算':
    bigfilepath = fileopenbox(title='MD5哈希值计算器', msg='请选择所需要计算MD5的文件！', default='*.zip')
    if bigfilepath==None:
        exit(-1)
    else:
        msgbox(title='MD5哈希值计算器',msg='所选文件%s的MD5值为:\n'% (bigfilepath) + getBigFileMD5(bigfilepath),ok_button='确认')