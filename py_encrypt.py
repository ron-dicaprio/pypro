#-*- coding:utf-8 -*-
#!/usr/bin/env python

from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QTextBrowser,QPushButton,QMessageBox,QLabel,QComboBox
from PyQt5.QtGui import QIcon
import sys,hashlib,base64

class py_encrypt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 加解密按钮
        self.buttonClicked1()
        self.buttonClicked2()
        
    def initUI(self):
        self.setWindowTitle('encrypt toolkit v1.0')
        self.setWindowIcon(QIcon('../pyfile/logo.png'))
        # 自定义窗口大小
        self.resize(600, 650)
        # windows窗口的位置
        self.move(700, 200)
        # 文本框位置
        self.text_area1 = QTextEdit(self)
        # 窗口位置
        self.text_area1.move(20, 80)
        self.text_area1.resize(440,260)
        #文本框位置
        self.text_area2 = QTextBrowser(self)
        #窗口位置
        self.text_area2.move(20, 350)
        #窗口区域大小
        self.text_area2.resize(440, 260)

        btn1 = QPushButton('加密', self)
        btn1.move(480, 80)
        btn1.resize(100,80)
        btn1.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        btn2 = QPushButton('解密', self)
        btn2.move(480, 180)
        btn2.resize(100,80)
        btn2.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")
        
        # 创建enceypt_type文本标签
        self.enceypt_type_label = QLabel(self)
        self.enceypt_type_label.move(10,20)
        self.enceypt_type_label.resize(65,30)
        self.enceypt_type_label.setText('加密方式:')
        
        # 创建enceypt_type下拉框
        self.denceypt_type_option = QComboBox(self)
        self.denceypt_type_option.move(80,20)
        self.denceypt_type_option.resize(230,30)

        # 设置下拉框可选项
        self.denceypt_type_option.addItems(['Base64','MD5','不加密'])
        # 设置下拉框的默认值
        self.denceypt_type_option.setCurrentIndex(0)
        
        self.show()
        self.statusBar().showMessage('兴趣永远是最好的老师！')
        btn1.clicked.connect(self.buttonClicked1)
        btn2.clicked.connect(self.buttonClicked2)

    # 获取索引号
    def get_encrypt_index(self):
        encrypt_index = self.denceypt_type_option.currentIndex()
        return encrypt_index

    # 获取索引内容
    def get_encrypt_Text(self):
        encrypt_text = self.denceypt_type_option.currentText()
        return encrypt_text

    # 加密按钮
    def buttonClicked1(self):
        textcontenct = self.text_area1.toPlainText()
        if textcontenct == '':
            pass
        else:
            self.text_area2.clear()
            # 获取加密方式，数组索引
            encrypt_text = self.get_encrypt_Text()
            print(encrypt_text)
            # 加密主窗口
            result = hashlib.md5(textcontenct.encode(encoding='UTF-8')).hexdigest().upper()
            # 获取md5加密值大写
            self.text_area2.append(result)
            self.statusBar().showMessage("[%s]加密成功！" % (textcontenct))

    # 解密按钮
    def buttonClicked2(self):
        textcontenct = self.text_area1.toPlainText()
        if textcontenct == '':
            pass
        else:
            self.text_area2.clear()
            # 解密主窗口

            result = hashlib.md5(textcontenct.encode(encoding='UTF-8')).hexdigest().upper()
            # 获取md5加密值大写
            self.text_area2.append(result)
            self.statusBar().showMessage("[%s]解密成功！" % (textcontenct))
        # print('time2:',time.time())

    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = py_encrypt()
    sys.exit(app.exec_())

'''
class Qtapp():
    def __init__(self):
        # 创建程序主窗口
        self.window = QMainWindow()
        self.window.resize(940,800)
        self.window.move(100,100)
        # self.window.setWindowTitle('自动化运维')
        # self.window.QIcon('../pyfile/logo.png')
        # 创建device_type文本标签
        self.device_type_label = QLabel(self.window)
        self.device_type_label.move(10,10)
        self.device_type_label.resize(65,30)
        self.device_type_label.setText('设备厂家:')

        # 创建device_type下拉框
        self.device_type_option = QComboBox(self.window)
        self.device_type_option.move(80,10)
        self.device_type_option.resize(90,30)
        self.device_type_option.addItem('Huawei')
        self.device_type_option.addItem('H3C')
        self.device_type_option.addItem('Cisco')
        self.device_type_option.addItem('juniper')

        self.protocol_label = QLabel(self.window)
        self.protocol_label.move(190,10)
        self.protocol_label.resize(50,30)
        self.protocol_label.setText('协议: ')

        self.protocol_option = QComboBox(self.window)
        self.protocol_option.move(230,10)
        self.protocol_option.resize(80,30)
        self.protocol_option.addItem('SSH')
        self.protocol_option.addItem('Telnet')

        self.username_label = QLabel(self.window)
        self.username_label.move(10,50)
        self.username_label.resize(50,30)
        self.username_label.setText('用户名: ')

        self.username_lineEdit = QLineEdit(self.window)
        self.username_lineEdit.move(80,50)
        self.username_lineEdit.resize(230,30)
        self.username_lineEdit.setPlaceholderText('请输入用户名')

        self.password_label = QLabel(self.window)
        self.password_label.move(10,90)
        self.password_label.resize(60,30)
        self.password_label.setText('密 码: ')

        self.password_lineEdit = QLineEdit(self.window)
        self.password_lineEdit.move(80,90)
        self.password_lineEdit.resize(230,30)
        self.password_lineEdit.setPlaceholderText('请输入密码')

        self.inspection_button = QPushButton(self.window)
        self.inspection_button.move(470,20)
        self.inspection_button.resize(150,100)
        self.inspection_button.setText('加密数据')
        self.inspection_button.clicked.connect(self.clickConfigurationButton)

        self.configuration_button = QPushButton(self.window)
        self.configuration_button.move(630,20)
        self.configuration_button.resize(150,100)
        self.configuration_button.setText('解密数据')
        self.configuration_button.clicked.connect(self.clickConfigurationButton)

        # **********************************************

        self.device_list_label = QLabel(self.window)
        self.device_list_label.move(10,150)
        self.device_list_label.resize(60,30)
        self.device_list_label.setText('设备列表')

        self.device_list_add_btn = QPushButton(self.window)
        self.device_list_add_btn.move(110,150)
        self.device_list_add_btn.resize(50,30)
        self.device_list_add_btn.setText('添加')

        self.device_list_del_btn = QPushButton(self.window)
        self.device_list_del_btn.move(160,150)
        self.device_list_del_btn.resize(50,30)
        self.device_list_del_btn.setText('删除')

        self.device_list_import_btn = QPushButton(self.window)
        self.device_list_import_btn.move(210,150)
        self.device_list_import_btn.resize(50,30)
        self.device_list_import_btn.setText('导入')

        self.device_list_clear_btn = QPushButton(self.window)
        self.device_list_clear_btn.move(260,150)
        self.device_list_clear_btn.resize(50,30)
        self.device_list_clear_btn.setText('清除')


        self.command_list_label = QLabel(self.window)
        self.command_list_label.move(320,150)
        self.command_list_label.resize(60,30)
        self.command_list_label.setText('命令列表')

        self.command_list_add_btn = QPushButton(self.window)
        self.command_list_add_btn.move(420,150)
        self.command_list_add_btn.resize(50,30)
        self.command_list_add_btn.setText('添加')

        self.command_list_del_btn = QPushButton(self.window)
        self.command_list_del_btn.move(470,150)
        self.command_list_del_btn.resize(50,30)
        self.command_list_del_btn.setText('删除')

        self.command_list_import_btn = QPushButton(self.window)
        self.command_list_import_btn.move(520,150)
        self.command_list_import_btn.resize(50,30)
        self.command_list_import_btn.setText('导入')

        self.command_list_clear_btn = QPushButton(self.window)
        self.command_list_clear_btn.move(570,150)
        self.command_list_clear_btn.resize(50,30)
        self.command_list_clear_btn.setText('清除')


        self.exec_res_label = QLabel(self.window)
        self.exec_res_label.move(630,150)
        self.exec_res_label.resize(60,30)
        self.exec_res_label.setText('执行结果')

        # *************************************

        self.device_list_textEdit = QPlainTextEdit(self.window)
        self.device_list_textEdit.move(10,190)
        self.device_list_textEdit.resize(300,600)

        self.command_list_textEdit = QPlainTextEdit(self.window)
        self.command_list_textEdit.move(320,190)
        self.command_list_textEdit.resize(300,600)

        self.exec_res_textEdit = QPlainTextEdit(self.window)
        self.exec_res_textEdit.move(630,190)
        self.exec_res_textEdit.resize(300,600)

    def initUI(self):
        self.setWindowTitle('encrypt toolkit v1.0')
        self.setWindowIcon(QIcon('../pyfile/logo.png'))

    def getUsername(self):
        return self.username_lineEdit.text()

    def getPassword(self):
        return self.password_lineEdit.text()

    def getDeviceList(self):
        return self.device_list_textEdit.toPlainText()

    def getCommandList(self):
        return self.command_list_textEdit.toPlainText()

    def clickConfigurationButton(self):
        username = self.getUsername()
        password = self.getPassword()
        device_list = self.getDeviceList()
        command_list = self.getCommandList()
        if username.strip() == '' or password.strip() == '':
            print('用户名和密码不能为空!')
        elif device_list == '':
            print('设备列表不能为空!')
        elif command_list == '':
            print('命令列表不能为空!')

if __name__ == '__main__':
    app = QApplication([])
    qt_app = Qtapp()
    qt_app.window.show()



    app.exec_() #执行程序,开始事件循环



# -*- coding:utf-8 -*-
# !/usr/bin/env python

import easygui
import pandas

# header参数定义首列位置
df = pandas.read_excel('D:\\Personal_doc\\pyfile\\dataform.xlsx',header=0)

# 展示所有列名称
print(df.columns)

# 展示特定列的值
print(df['bidname_list'])

import easygui, video_cut,os
# 获取用户选择的功能
user_choice = easygui.choicebox(title='python视频编辑器',msg='请选择对应的功能',choices=['合并视频','剪切视频'])
print(user_choice)
if user_choice == '合并视频':
    file_list = easygui.fileopenbox(title='python视频编辑器',msg='请选择需要合并的视频文件',default='*.mp4',multiple=True)
    # 增加过滤，防止报错。file_list参数非空且文件长度大于1个
    if file_list is not None and len(file_list) > 1:
        # 定义保存的文件名称，默认为savefile.MP4
        filesave_path = easygui.filesavebox(title='python视频编辑器',msg='请选择视频文件保存位置',default='savefile.mp4')
        if filesave_path is not None:
            print(file_list,filesave_path)
            try:
                video_cut.py_combfilesAV(file_list, filesave_path)
                print('files are combined!')
            except Exception as e:
                print(e)
elif user_choice == '剪切视频':
    print('剪切视频')


#-*-coding:utf-8-*_
#!/bin/env python
import folium
import webbrowser
import os
def py_maps(x,y):
    py_map = folium.Map(
        # 坐标跟实际坐标相反
        location=[y, x],
        # 比例尺，默认为10级
        zoom_start=15,
        # 地图的长和宽
        width='100%',
        height='100%',
        # 地图样式，默认为OpenStreetMap
        tiles='OpenStreetMap',
        # 是否添加比例尺
        control_scale=False,
    )
    if os.path.exists('maps.html'):
        os.remove('maps.html')
    py_map.save('maps.html')
    webbrowser.open('maps.html')
def main():
    pass
if __name__ == '__main__':
    main()

py_maps(112.918384,28.138008)
from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QTextBrowser,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
import sys,time,hashlib,base64

# print('time1:', time.time())
class py_encrypt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 定义加解密按钮
        self.buttonClicked1()
        #self.buttonClicked2()

    def initUI(self):
        self.setWindowTitle('encrypt toolkit v1.0')
        self.setWindowIcon(QIcon('../pyfile/logo.png'))
        # 自定义窗口大小
        self.resize(600, 700)
        # windows窗口的位置
        self.move(700, 200)
        # 文本框位置
        self.text_area1 = QTextEdit(self)
        # 窗口位置
        self.text_area1.move(20, 20)
        self.text_area1.resize(440,280)
        #文本框位置
        self.text_area2 = QTextBrowser(self)
        #窗口位置
        self.text_area2.move(20, 350)
        #窗口区域大小
        self.text_area2.resize(440, 288)

        btn1 = QPushButton('加密', self)
        btn1.move(480, 80)

        btn2 = QPushButton('解密', self)
        btn2.move(480, 180)

        self.show()
        self.statusBar().showMessage('兴趣永远是最好的老师！')
        btn1.clicked.connect(self.buttonClicked1)

        #btn2.clicked.connect(self.buttonClicked2)


    # 加密按钮
    def buttonClicked1(self):
        textcontenct = self.text_area1.toPlainText()
        if textcontenct == '':
            pass
        else:
            self.text_area2.clear()
            #result = py_translate.youdao_translate(textcontenct)
            # 加密主窗口

            result = hashlib.md5(textcontenct.encode(encoding='UTF-8'))
            # 获取md5加密值大写
            self.text_area2.append(result.hexdigest().upper())
            self.statusBar().showMessage("[%s]加密成功！" % (result))
        # print('time2:',time.time())

    # 解密按钮
    def buttonClicked2(self):
        textcontenct = self.text_area1.toPlainText()
        if textcontenct == '':
            pass
        else:
            self.text_area2.clear()
            #result = py_translate.youdao_translate(textcontenct)
            # 解密主窗口

            result = hashlib.md5(textcontenct.encode(encoding='UTF-8'))
            # 获取md5加密值大写
            self.text_area2.append(result.hexdigest().upper())
            self.statusBar().showMessage("[%s]加密成功！" % (result))
        # print('time2:',time.time())

    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = py_encrypt()
    sys.exit(app.exec_())




# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import py_translate
import sys

class tanslate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buttonClicked()

    def initUI(self):
        self.setWindowTitle('有道翻译器V1.0')

        self.setWindowIcon(QIcon('logo.png'))
        # 自定义窗口大小
        self.resize(600, 700)
        # windows窗口的位置
        self.move(700, 200)
        #增加按钮
        btn1 = QPushButton("确认翻译", self)
        #按钮位置
        btn1.move(0, 100)
        #文本框位置
        self.text_area1 = QTextEdit(self)
        #窗口位置
        self.text_area1.move(100, 40)
        #窗口区域大小
        self.text_area1.resize(450, 300)

        #增加按钮
        btn2 = QLabel("翻译结果", self)
        #按钮位置
        btn2.move(20, 400)
        #文本框位置
        self.text_area2 = QTextBrowser(self)
        #窗口位置
        self.text_area2.move(100, 380)
        #窗口区域大小
        self.text_area2.resize(450, 300)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('菜单')
        #fileMenu2 = menubar.addMenu('工具')
        #fileMenu3 = menubar.addMenu('帮助')
        impMenu = QMenu('翻译器', self)
        #impMenu2 = QMenu('开发者', self)
        impAction = QAction('确认翻译', self)
        #impAction2 = QAction('关于软件', self)
        impMenu.addAction(impAction)
        #impMenu2.addAction(impAction2)
        fileMenu.addMenu(impMenu)
        #fileMenu2.addMenu(impMenu2)
        self.show()
        btn1.clicked.connect(self.buttonClicked)
        self.statusBar().showMessage("有道词典V1.0")
        #impAction.clicked.connect(self.buttonClicked2)


    def buttonClicked(self):
        #判断要翻译的内容是否为空
        textcontenct = self.text_area1.toPlainText()
        #内容为空就不调用接口
        if textcontenct == '':
            pass
        else:
            try:
                result = py_translate.youdao_translate(textcontenct)
                self.text_area2.clear()
                self.text_area2.append(result)
                self.statusBar().showMessage("%s 翻译完毕！" % (textcontenct))

            except Exception as e:
                print(self.text_area2.append(e))


    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    #键盘退出事件
    #def keyPressEvent(self, esc):
    #    if esc.key() == Qt.Key_Escape:
    #       self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = tanslate()
    sys.exit(app.exec_())
  
'''
