# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 15:25
# @Author  : Yaojie Chang
# @File    : search_GUI.py
# @Software: PyCharm
import time
from PyQt5.QtWidgets import QWidget, QMessageBox

from MyGUI.search_window import Ui_SearchWindow
# from search_window import Ui_SearchWindow


class SearchWindow(QWidget, Ui_SearchWindow):
    def __init__(self):
        super(SearchWindow, self).__init__()
        self.setupUi(self)

        self.chat_obj = None

        self.pushButton_search.clicked.connect(self.search_user)
        self.listWidget_result.doubleClicked.connect(self.add_friend)

    def get_chat_obj(self, chat_obj):
        self.chat_obj = chat_obj

    def search_user(self):      # 只管发送查找请求, 然后返回信息统一处理
        keyword = str(self.lineEdit_keyword.text())
        if keyword == '':
            QMessageBox.warning(self, '关键词为空', '关键词为空!!!')
            return
        self.chat_obj.search_users(keyword)

    def add_friend(self):
        username = self.listWidget_result.currentItem().text()
        reply = QMessageBox.question(self, '添加好友', '你将要添加 '+username+' 为好友,是否添加?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.chat_obj.add_friend(username)
            QMessageBox.information(self, '添加成功', '您已成功添加 ' + username + ' 为好友')
