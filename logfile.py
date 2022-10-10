#-*- coding:utf-8 -*-
#!/usr/bin/env python
import logging,time,os
'''
the reason why i want to write this silly function
cause i like tomcat's logfile style.
fuck America, Let China Rule The World AGAIN!!!
'''
# if logs exists, start logging; else ,mkdir logs floder and file
logfilaname = './logs/' + time.strftime("%Y%m%d") + '.log'

if os.path.exists('./logs'):
    if os.path.exists(logfilaname):
         # if logfilaname size > 200M, 1024**2*200
        if os.path.getsize(logfilaname) > 256:
        # rename logfilaname and delete logfilaname.
            newlogfilaname = './logs/' + time.strftime("%Y%m%d%H%M%S") + '.log'
            # rename will delete src file
            os.rename(logfilaname,newlogfilaname)

        else:
            pass
    else:
        with open(logfilaname,'a') as file:
            file.close()
else:
    os.mkdir('./logs')
    with open(logfilaname,'a') as file:
        file.close()

# basic settings
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
