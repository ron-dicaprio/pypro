#-*- coding:utf-8 -*-
#!/usr/bin/env python
from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QTextBrowser,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
import sys,time,socket

class pyqt_im(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 加解密按钮
        self.buttonClicked1()
        self.buttonClicked2()
        
    def initUI(self):
        self.setWindowTitle('python socket 即时通讯工具v1.0')
        self.setWindowIcon(QIcon('../../pyfile/favicon.ico'))
        # windows窗口的位置
        self.move(500, 100)
        # 自定义窗口大小
        self.resize(950, 700)

        # 文本框位置QTextBrowser
        self.text_area1 = QTextBrowser(self)
        # 窗口位置
        self.text_area1.move(20, 20)
        self.text_area1.resize(910,350)
        self.text_area1.setStyleSheet("font-weight: bold; font-size: 13px; font-family: Microsoft YaHei UI")
        #文本框位置
        self.text_area2 = QTextEdit(self)
        #窗口位置
        self.text_area2.move(20, 400)
        #窗口区域大小
        self.text_area2.resize(750, 250)
        self.text_area2.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        btn1 = QPushButton('发送', self)
        btn1.move(800, 400)
        btn1.resize(100,80)
        btn1.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        btn2 = QPushButton('清空', self)
        btn2.move(800, 570)
        btn2.resize(100,80)
        btn2.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")
        
        # 点击事件
        btn1.clicked.connect(self.buttonClicked1)
        btn2.clicked.connect(self.buttonClicked2)
        
        self.show()
        self.statusBar().showMessage('兴趣永远是最好的老师！')
            
    def socketMQ(self,data):
        ip='43.139.80.246'
        port=10240
        # 创建TCP套接字
        client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_sock.connect((ip,port))
        client_sock.send(data.encode())
        # 打印返回的消息
        return bytes.decode(client_sock.recv(4096))



    # 发送按钮
    def buttonClicked1(self):
        textcontenct = self.text_area2.toPlainText()
        if textcontenct == '':
            pass
        else:
            
            textcontenct=str(time.strftime("%Y-%m-%d %H:%m:%S"))+' : '+textcontenct
            self.text_area1.append(textcontenct)
            self.text_area2.clear()
            self.statusBar().showMessage("消息<%s>发送成功！" % (textcontenct))
            res = self.socketMQ(textcontenct)
            self.text_area1.append(res)
        
      
    # 清空按钮
    def buttonClicked2(self):
        self.text_area1.clear()

    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = pyqt_im()
    sys.exit(app.exec_())