# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 16:00
# @Author  : Yaojie Chang
# @File    : register_GUI.py
# @Software: PyCharm
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

# from MyGUI.register_window import Ui_RegisterWindow
from register_window import Ui_RegisterWindow


class RegisterWindow(QWidget, Ui_RegisterWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)

        self.chat_obj = None

        self.pushButton_register.clicked.connect(self.register_submit)

    def register_submit(self):
        username = str(self.lineEdit_username.text())
        if username == '':
            QMessageBox.warning(self, '不能为空', '用户名不能为空!!!')
            return
        password = str(self.lineEdit_password.text())
        re_password = str(self.lineEdit_re_password.text())
        if password == '' or password != re_password:
            QMessageBox.warning(self, '密码不匹配', '两次输入的密码不一致或为空!!!')
            return
        self.chat_obj.send_msg(content={'username': username, 'password': password}, send_type='register')
        response = self.chat_obj.recv_msg()
        if response.get('code', 1) == 0:
            QMessageBox.information(self, '注册成功', response.get('result', '注册成功!!!'))
            self.hide()
        else:
            QMessageBox.warning(self, '注册失败', response.get('result', '该用户名已存在!!!'))

    def get_chat_obj(self, chat_obj):
        self.chat_obj = chat_obj


