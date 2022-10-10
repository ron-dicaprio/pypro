#-*- coding:utf-8 -*-
#!/usr/bin/env python
import logging,time,os
'''
the reason why i want to write this silly function
i like tomcat's logfile style.
fuck America, Let China Rule The World AGAIN!!!
'''
# if floder exists, start logging; else , mkdir logs floder
if os.path.exists('./logs'):
    logfilaname = './logs/' + time.strftime("%Y%m%d") + '.log'
    with open(logfilaname,'a+') as file:
        file.close()
    # if logfilaname size > 200M
    if os.path.getsize(logfilaname) > 1024**2*200:
        # rename logfilaname and delete logfilaname.
        newlogfilaname = './logs/' + time.strftime("%Y%m%d%H%M%S") + '.log'
        os.rename(logfilaname,newlogfilaname)
        os.remove(logfilaname)
    else:
        pass
else:
    os.mkdir('./logs')
    logfilaname = './logs/' + time.strftime("%Y%m%d") + '.log'
logging.basicConfig(filename=logfilaname,filemode='a+',level=logging.INFO,encoding='utf-8',format='#### %(asctime)s | %(levelname)s | %(message)s')
def critical(self):
    return logging.critical(self)

def error(self):
    return logging.error(self)

def warning(self):
    return logging.warning(self)

def info(self):
    return logging.info(self)

def debug(self):
    return logging.debug(self)
