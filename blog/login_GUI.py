# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 8:34
# @File    : test2.py
# @Software: PyCharm
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from login_window import Ui_LoginWindow
from users_lists_GUI import UsersListsWindow
from register_GUI import RegisterWindow

# from MyGUI.client_v12 import SFChatClient
from client import SFChatClient


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.users_lists_window = UsersListsWindow()
        self.register_window = RegisterWindow()

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
            threading.Thread(target=self.recv_msg_always, args=(chat_obj,)).start()
            self.users_lists_window.get_online_users()
            self.users_lists_window.label_username.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">"+chat_obj.username+"</span></p></body></html>")
        else:
            QMessageBox.warning(self, '登陆失败!!!', '用户名或密码错误!!!')

    def pushButton_register_click(self):
        try:
            chat_obj = SFChatClient()
        except:
            QMessageBox.warning(self, '网络出错', '链接服务器失败，请检查网络或联系管理员!!!')
            return
        self.register_window.get_chat_obj(chat_obj)
        self.register_window.show()

    def recv_msg_always(self, chat_obj):
        while True:
            recv_dict = chat_obj.recv_msg()
            if recv_dict.get('send_type', '') == 'msg':
                content = recv_dict.get('content', '')
                send_time = recv_dict.get('send_time', '')
                from_user = recv_dict.get('from_user', '')
                print(send_time + '\n收到来自' + from_user + '的消息:' + content)
                self.users_lists_window.listWidget_recv_msg.addItem(send_time + '//' + from_user + ' : ' + content)
            elif recv_dict.get('send_type', '') == 'logout':
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())



