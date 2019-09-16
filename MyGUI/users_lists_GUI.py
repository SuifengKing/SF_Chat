# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 10:12
# @Author  : Yaojie Chang
# @File    : users_lists_GUI.py
# @Software: PyCharm
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QListWidgetItem

# from MyGUI.users_lists_window import Ui_UsersLists
from users_lists_window import Ui_UsersLists


class UsersListsWindow(QWidget, Ui_UsersLists):
    def __init__(self):
        super(UsersListsWindow, self).__init__()
        self.setupUi(self)

        self.chat_obj = None
        self.send_to = ''

        self.listWidget_online_users.doubleClicked.connect(lambda: self.start_chat(self.listWidget_online_users))
        self.listWidget_friends.doubleClicked.connect(lambda: self.start_chat(self.listWidget_friends))
        self.pushButton_fresh_online_users.clicked.connect(self.get_online_users)
        self.pushButton_send_msg.clicked.connect(self.send_msg)
        self.pushButton_exit.clicked.connect(self.log_out_exit)

    def start_chat(self, listwidget):
        print(listwidget.currentItem().text())
        self.send_to = listwidget.currentItem().text()
        self.label_user_to.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">正在给'+listwidget.currentItem().text()+'发送消息</span></p></body></html>')

    def send_msg(self):
        text = self.textEdit_msg_edit.toPlainText()
        if text == '':
            QMessageBox.warning(self, '内容为空', '内容不能为空!!!')
            return
        if self.send_to == '':
            QMessageBox.warning(self, '未选择接收用户', '请双击左侧列表用户名选择接收用户!!!')
            return
        self.chat_obj.send_msg(content={'content': text}, send_to=self.send_to)
        self.textEdit_msg_edit.clear()

    def get_chat_obj(self, chat_obj):
        self.chat_obj = chat_obj
        self.setWindowTitle(self.chat_obj.username)

    def get_online_users(self):
        self.listWidget_online_users.clear()
        self.chat_obj.get_users_list()
        time.sleep(1.5)
        for user in self.chat_obj.online_users_list:
            self.listWidget_online_users.addItem(user)

    def log_out_exit(self):
        self.chat_obj.send_msg(content={}, send_type='logout')
        self.close()






