#!/usr/bin/env python
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def py_email(subject, message_con, to_user):
    to_user=[to_user]
    from_user = '1102346940@qq.com'
    # 不要动我的passwd！
    from_passwd = 'passwd'
    mail_server = smtplib.SMTP('smtp.qq.com', 25)
    mail_server.login(from_user, from_passwd)
    # filepaths = filepaths.replace('/','\\')
    # 构建一个邮件实例
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_user
    message['To'] = ';'.join(to_user)
    message.attach(MIMEText(message_con, 'plain', 'utf-8'))
    '''
    # 并不需要发送附件，暂时先取消该功能。
    for filenames in (filepaths.split(';')):
        attachfile = MIMEText(open(filenames, 'rb').read(), 'base64', 'utf-8')
        attachfile["Content-Type"] = 'application/octet-stream'
        attachfile["Content-Disposition"] = 'attachment; filename=%s' % (str(filenames).split('\\')[-1])
        message.attach(attachfile)
    '''
    try:
        #starttime = time.time()
        mail_server.sendmail(from_user, message['To'].split(';'), message.as_string())
        print('email send success!')
        #endtime = time.time()
        #print('email cost',endtime-starttime,'secends')
    except Exception as e:
        print(e)
        mail_server.quit()


#钉钉报警
import requests,json
# 这里改为自己创建的机器人的webhook地址
webhook="https://oapi.dingtalk.com/robot/send?access_token='my_token'"
# 接受脚本运行时传的参数 第一个为手机号 第二个参数随意 第三个为内容， 直接写在函数里面算了
# user=sys.argv[1]
# text=sys.argv[3]
def pydingtalk(user, email, text):
    # 设置了keyword验证，必须带上对应的字样
    text='智能小助手：' + text + '\n'
    text.encode(encoding='utf-8')
    data={
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                user #需要@群手机号码对应的人
            ],
            "isAtAll": True #是否全部@，True为是,False为否，但参数为ALL时再at特定人员，则at无效
            }
	}
    headers = {'Content-Type': 'application/json'}
    x=requests.post(url=webhook, data=json.dumps(data), headers=headers)

    # 打印一下返回的json字符串
    print(x.json())
    # {u'errcode': 0, u'errmsg': u'ok'}
    # 发送邮件通知相关人员，这里做一个开关最好！
    py_email('a system error occurd!', text, email)

# 执行程序
pydingtalk(18073819450, '1102346940@qq.com', '大家早上好啊！亲爱的摸鱼者们！')
