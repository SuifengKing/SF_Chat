# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 10:12
# @Author  : Yaojie Chang
# @File    : users_lists_GUI.py
# @Software: PyCharm
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListWidgetItem
from PyQt5.QtGui import QPixmap

from MyGUI.users_lists_window import Ui_UsersLists
from MyGUI.search_GUI import SearchWindow
# from users_lists_window import Ui_UsersLists
# from search_GUI import SearchWindow


class UsersListsWindow(QWidget, Ui_UsersLists):
    def __init__(self):
        super(UsersListsWindow, self).__init__()
        self.setupUi(self)

        self.chat_obj = None
        self.send_to = ''

        self.search_window = None

        self.label_show.setPixmap(QPixmap('tushansusu.jpg'))    # 窗口右侧的形象展示
        self.listWidget_online_users.doubleClicked.connect(lambda: self.start_chat(self.listWidget_online_users))
        self.listWidget_friends.doubleClicked.connect(lambda: self.start_chat(self.listWidget_friends))
        self.pushButton_fresh_online_users.clicked.connect(self.get_online_users)
        self.pushButton_fresh_friend_list.clicked.connect(self.get_friends)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_send_msg.clicked.connect(self.send_msg)
        self.pushButton_exit.clicked.connect(self.log_out_exit)

    def recv_msg_always(self, chat_obj):
        while True:
            recv_dict = chat_obj.recv_msg()
            send_type = recv_dict.get('send_type', '')
            if send_type == 'msg':
                content = recv_dict.get('content', '')
                send_time = recv_dict.get('send_time', '')
                from_user = recv_dict.get('from_user', '')
                self.listWidget_recv_msg.addItem(send_time + '//' + from_user + ' : ' + content)
            elif send_type == 'search_users':
                users_list = recv_dict.get('result', [])
                self.search_window.listWidget_result.clear()
                for user in users_list:
                    self.search_window.listWidget_result.addItem(user)
            elif recv_dict.get('send_type', '') == 'logout':
                break

    def start_chat(self, listwidget):
        print(listwidget.currentItem().text())
        self.send_to = listwidget.currentItem().text()
        self.label_user_to.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">正在给'+listwidget.currentItem().text()+'发送消息</span></p></body></html>')

    def send_msg(self):
        text = self.textEdit_msg_edit.toPlainText()
        if text == '':
            QMessageBox.warning(self, '内容为空', '内容为空!!!')
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

    def get_friends(self):
        self.listWidget_friends.clear()
        self.chat_obj.get_friends_list()
        time.sleep(1)
        for friend in self.chat_obj.friends_list:
            self.listWidget_friends.addItem(friend)

    def search(self):
        self.search_window = SearchWindow()
        self.search_window.get_chat_obj(self.chat_obj)
        self.search_window.show()

    def log_out_exit(self):
        self.chat_obj.send_msg(content={}, send_type='logout')
        self.close()






