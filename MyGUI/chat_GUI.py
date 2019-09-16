# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 10:20
# @Author  : Yaojie Chang
# @File    : chat_GUI.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# from MyGUI.chat_window import Ui_ChatWindow
from chat_window import Ui_ChatWindow


class ChatWindow(QWidget, Ui_ChatWindow):
    def __init__(self):
        super(ChatWindow, self).__init__()
        self.setupUi(self)

