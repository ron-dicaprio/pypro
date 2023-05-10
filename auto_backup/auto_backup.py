#-*- coding:utf-8 -*-
# 备份脚本，配合windows的计划任务实现
import os,configparser,shutil,time
def auto_backup():
    try:
        config = configparser.ConfigParser()
        config.read("auto_backup.ini",encoding='utf-8')
        key_src=config.get("auto_backup", "src") 
        key_des=config.get("auto_backup", "des")
        logfile=config.get("auto_backup", "logfile")
        is_save_src=config.get("auto_backup", "is_save_src")
        #print(key_src,key_des,logfile)
        if os.path.exists(key_src):
            pass
        else:
            os.mkdir(key_src)
        if os.path.exists(key_des):
            pass
        else:
            os.mkdir(key_des)
            
        key_des=key_des+'\\'+time.strftime("%Y%m%d%H%M%S")

        shutil.copytree(key_src, key_des)

        with open(logfile,"a",encoding="utf-8") as file:
            file.write('%s | 备份成功！，备份文件路径为：%s\n' % (time.strftime("%Y-%m-%d %H:%M:%S"), key_des))

        if is_save_src=='0':
            shutil.rmtree(key_src)
            os.mkdir(key_src)

    except Exception as E:
        print("备份失败")
        print(E)
        time.sleep(10)
        with open(logfile,'a') as file:
            file.write('%s | 备份失败！\n' % (time.strftime("%Y-%m-%d %H:%M:%S")))
            file.write('%s:%s \n' % (time.strftime("%Y-%m-%d %H:%M:%S"), E))

if __name__=='__main__':
    auto_backup()
