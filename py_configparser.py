# pymysql engine to run sql command.
import pymysql,configparser
def pyrunsql(self):
    # 实例化ConfigParser
    try:    
        config = configparser.ConfigParser() 
        config.read("dbconf.cfg")
        #print(config.sections())
        key_host=config.get("dockerhost", "host") 
        key_port=config.get("dockerhost", "port") 
        key_user=config.get("dockerhost", "dbuser")
        key_passwd=config.get("dockerhost", "dbpasswd")
        key_db=config.get("dockerhost", "db")
        conn = pymysql.connect(host=key_host,port=int(key_port),user=key_user, passwd=key_passwd, db=key_db,charset='utf8mb4')
        cur = conn.cursor()
        cur.execute(self)
        conn.commit()
        conn.close()
        #print('sql execute succsess!')
        return cur.fetchall()
    except Exception as ERROR:
        return ERROR

    
#dbconfig
[dockerhost]
host=172.31.65.168
port=3306
dbuser=root
dbpasswd=@Caitao628422
db=epointoneapm


[db_name]
name='zhangsan'
