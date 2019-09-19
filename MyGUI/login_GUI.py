# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 8:34
# @Author  : Yaojie Chang
# @File    : test2.py
# @Software: PyCharm
import time
import threading
import sys
# import os
# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

from MyGUI.login_window import Ui_LoginWindow
from MyGUI.users_lists_GUI import UsersListsWindow
from MyGUI.register_GUI import RegisterWindow
# from login_window import Ui_LoginWindow
# from users_lists_GUI import UsersListsWindow
# from register_GUI import RegisterWindow

from MyGUI.client_v12 import SFChatClient
# from client_v12 import SFChatClient


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.users_lists_window = UsersListsWindow()
        self.register_window = None

        self.pushButton_login.clicked.connect(self.pushButton_login_click)
        self.pushButton_register.clicked.connect(self.pushButton_register_click)

    def pushButton_login_click(self):
        username = str(self.lineEdit_username.text())
        password = str(self.lineEdit_password.text())
        try:
            chat_obj = SFChatClient()
            chat_obj.login(username=username, password=password)
        except:
            QMessageBox.warning(self, '网络出错', '链接服务器失败，请检查网络或联系管理员!!!')
            return
        if chat_obj.is_login:
            self.users_lists_window.get_chat_obj(chat_obj)
            self.users_lists_window.show()
            self.hide()
            threading.Thread(target=self.users_lists_window.recv_msg_always, args=(chat_obj,)).start()
            self.users_lists_window.get_online_users()
            self.users_lists_window.get_friends()
            self.users_lists_window.label_username.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">"+chat_obj.username+"</span></p></body></html>")
        else:
            QMessageBox.warning(self, '登陆失败!!!', '用户名或密码错误!!!')

    def pushButton_register_click(self):
        try:
            chat_obj = SFChatClient()
        except:
            QMessageBox.warning(self, '网络出错', '链接服务器失败，请检查网络或联系管理员!!!')
            return
        self.register_window = RegisterWindow()
        self.register_window.get_chat_obj(chat_obj)
        self.register_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

# self.my_checkbox.stateChanged.connect(self.related_function)  # 将checkbox状态变化事件连接相应函数
# self.my_checkbox.isChecked()  # 检查checkbox是否被勾选
# self.my_checkbox.setCheckState(QtCore.Qt.Unchecked)  # 将checkbox状态设置为未勾选状态
# QtCore.Qt.Checked 为勾选状态

# self.image_type_comboBox.currentIndex()   # 获取当前选项的Index（int）
# self.image_type_comboBox.currentText()    # 获取当前选项的文本（Qstring）

# Movie = QMovie('time.gif')  # 载入Gif图，注意QMovie在PyQt5.QtCore内
# self.movie_label.setMovie(Movie)  # 将gif显示在gif中
# Movie.start()  # 启动gif
# Movie.stop()   # 停止gif


