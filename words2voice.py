#-*- coding:utf-8 -*-
#!/usr/bin/env python
from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QPushButton,QMessageBox,QLabel,QComboBox
from PyQt5.QtGui import QIcon
import sys,pyttsx3,time,os
class words2voice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 右侧按钮
        self.ButtonClicked1()
        self.ButtonClicked2()
        self.ButtonClicked3()
        self.ButtonClicked4()
        
    def initUI(self):
        self.setWindowTitle('文字语音输出工具V1.0')
        self.setWindowIcon(QIcon('images/favicon.ico'))
        #self.resize(600, 650)
        # 固定窗口大小
        self.setFixedSize(600, 650)
        # windows窗口的位置
        self.move(700, 200)
        # 文本框位置
        self.text_area1 = QTextEdit(self)
        # 窗口位置
        self.text_area1.move(20, 80)
        self.text_area1.resize(440,520)
        self.text_area1.setStyleSheet("font-weight: bold; font-size: 18px; font-family: Consolas")

        btn1 = QPushButton('播放语音', self)
        btn1.move(480, 80)
        btn1.resize(100,80)
        btn1.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        btn2 = QPushButton('清除内容', self)
        btn2.move(480, 180)
        btn2.resize(100,80)
        btn2.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        btn3 = QPushButton('保存语音', self)
        btn3.move(480, 280)
        btn3.resize(100,80)
        btn3.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")
        
        btn4 = QPushButton('打开文件', self)
        btn4.move(480, 380)
        btn4.resize(100,80)
        btn4.setStyleSheet("font-weight: bold; font-size: 20px; font-family: Microsoft YaHei UI")

        # 创建lang_type_label文本标签
        self.lang_type_label = QLabel(self)
        self.lang_type_label.move(10,20)
        self.lang_type_label.resize(65,30)
        self.lang_type_label.setText('语言类型:')
        self.lang_type_label.setStyleSheet("font-weight: thin; font-size: 12px; font-family: Microsoft YaHei UI")
        
        # 创建lang_choice_option下拉框
        self.lang_choice_option = QComboBox(self)
        self.lang_choice_option.move(80,20)
        self.lang_choice_option.resize(150,30)

        # 设置下拉框可选项
        #self.lang_choice_option.addItems(['Base64','MD5','不加密'])
        self.lang_choice_option.addItems(['中文','英文'])
        # 设置下拉框的默认值
        self.lang_choice_option.setCurrentIndex(0)
        self.lang_choice_option.setStyleSheet("font-weight: thin; font-size: 12px; font-family: Microsoft YaHei UI")
        
        # 创建voice_type_label文本标签
        self.voice_type_label = QLabel(self)
        self.voice_type_label.move(300,20)
        self.voice_type_label.resize(65,30)
        self.voice_type_label.setText('音量大小:')
        self.voice_type_label.setStyleSheet("font-weight: thin; font-size: 12px; font-family: Microsoft YaHei UI")
        
               
        # 创建voice_choice_option下拉框
        self.voice_choice_option = QComboBox(self)
        self.voice_choice_option.move(380,20)
        self.voice_choice_option.resize(150,30)

        # 设置下拉框可选项
        self.voice_choice_option.addItems(['0.2','0.5','0.8','1.0'])
        # 设置下拉框的默认值
        self.voice_choice_option.setCurrentIndex(2)
        self.voice_choice_option.setStyleSheet("font-weight: thin; font-size: 12px; font-family: Microsoft YaHei UI") 
        
        self.show()
        self.statusBar().showMessage('兴趣永远是最好的老师！')
        btn1.clicked.connect(self.ButtonClicked1)
        btn2.clicked.connect(self.ButtonClicked2)
        btn3.clicked.connect(self.ButtonClicked3)
        btn4.clicked.connect(self.ButtonClicked4)

    '''
    # 获取索引号
    def get_encrypt_index(self):
        encrypt_index = self.lang_choice_option.currentIndex()
        return encrypt_index

    # 获取索引内容
    def get_encrypt_Text(self):
        encrypt_text = self.lang_choice_option.currentText()
        return encrypt_text
    '''

    def play_sound(self,words):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if self.lang_choice_option.currentText() == '中文':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        volume = engine.getProperty('volume')
        print(volume)
        choice_vol = self.voice_choice_option.currentText()
        engine.setProperty('volume', float(choice_vol))
        engine.say(words)
        engine.runAndWait()
        engine.stop()

    def save_sound(self,words):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if self.lang_choice_option.currentText() == '中文':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        volume = engine.getProperty('volume')
        print(volume)
        choice_vol = self.voice_choice_option.currentText()
        engine.setProperty('volume',float(choice_vol))
        engine.say(words)
        filepath = 'D:\\voice\\' + time.strftime("%Y%m%d%H%M%S") + '.mp3'
        engine.save_to_file(words, filepath)
        engine.runAndWait()
        engine.stop()
        self.statusBar().showMessage("音频保存成功，保存路径为:%s" % (filepath))

    # 播放按钮
    def ButtonClicked1(self):
        textcontenct = self.text_area1.toPlainText()
        # 过滤掉空值
        if textcontenct == '':
            self.statusBar().showMessage("输入内容为空，请确认！")
        else:
            # self.text_area1.clear()
            # 获取输入的文本
            self.play_sound(textcontenct)

    # 清除按钮
    def ButtonClicked2(self):
        self.text_area1.clear()
        # 主窗口
        self.statusBar().showMessage("清除成功！")

    # 保存按钮
    def ButtonClicked3(self):
        textcontenct = self.text_area1.toPlainText()
        # 过滤掉空值
        if textcontenct == '':
            self.statusBar().showMessage("输入内容为空，请确认！")
        else:
            # 获取输入的内容
            self.save_sound(textcontenct)

    # 打开文件按钮
    def ButtonClicked4(self):
        if os.path.exists('d:\\voice'):
            os.startfile('d:\\voice')
        else:
            os.mkdir('d:\\voice')
            os.startfile('d:\\voice')

    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = words2voice()
    sys.exit(app.exec_())


