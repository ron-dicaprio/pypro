#-*- coding:utf-8 -*-
#!/usr/bin/env python3
# 脚本任何报错都会退出，请去确认并核实。本脚本适用于debian系操作系统
# version v1.0
import redis,sys
from os import system
# 持久化redis pool
try:
    pool = redis.ConnectionPool(host='52.69.93.175', port=35379, decode_responses=True, db=0)
    rds = redis.Redis(connection_pool=pool)
except Exception as e:
    print('redis初始化失败!',e)
    sys.exit(-1)

# if exists keys
if rds.exists('docker-tomcat'):
    cur_ver=int(rds.get('docker-tomcat'))+1
    # cmd result code is int type.
    docker_builder_code=system("sudo docker build -t registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0 -f /data/docker-data/Dockerfile /data/docker-data/ > /dev/null" % (cur_ver))
    if docker_builder_code==0:
        print('镜像打包完毕，请确认!')
    else:
        print("镜像打包失败，系统自动退出!")
        sys.exit(-1)
    registry_login_code=system("sudo docker login -u 1102346940@qq.com -p @Caitao628422 registry.cn-hangzhou.aliyuncs.com > /dev/null")
    if registry_login_code==0:
        print("registry登陆成功!")
        img_push_code=system("sudo docker push registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0 > /dev/null" % (cur_ver))
        if img_push_code==0:
            print("镜像推送成功!","registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            system("sudo docker rm -f docker-tomcat")
            system("sudo docker run --name docker-tomcat -d -p 80:8080 registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            #system("sudo docker rmi registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
        else:
            print("镜像推送失败!")
            system("sudo docker rmi registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            sys.exit(-1)
    else:
        print("registry登陆失败!")
        sys.exit(-1)

    # 更新redis版本号
    rds.set('docker-tomcat',cur_ver)

# if not exists keys,set 1.
else:
    rds.set('docker-tomcat','0')
    cur_ver=int(rds.get('docker-tomcat'))+1
    # cmd result code is int type.
    docker_builder_code=system("sudo docker build -t registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0 -f /data/docker-data/Dockerfile /data/docker-data/ > /dev/null" % (cur_ver))
    if docker_builder_code==0:
        print('镜像打包完毕，请确认!')
    else:
        print("镜像打包失败，系统自动退出!")
        sys.exit(-1)
    registry_login_code=system("sudo docker login -u 1102346940@qq.com -p @Caitao628422 registry.cn-hangzhou.aliyuncs.com > /dev/null")
    if registry_login_code==0:
        print("registry登陆成功!")
        img_push_code=system("sudo docker push registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0 > /dev/null" % (cur_ver))
        if img_push_code==0:
            print("镜像推送成功!","registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            system("sudo docker rm -f docker-tomcat")
            system("sudo docker run --name docker-tomcat -d -p 80:8080 registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            #system("sudo docker rmi registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
        else:
            print("镜像推送失败!")
            system("sudo docker rmi registry.cn-hangzhou.aliyuncs.com/cait/docker-tomcat:v%s.0" % (cur_ver))
            sys.exit(-1)
    else:
        print("registry登陆失败!")
        sys.exit(-1)

    # 更新redis版本号
    rds.set('docker-tomcat',cur_ver)
