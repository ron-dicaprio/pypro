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
