# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users_lists_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UsersLists(object):
    def setupUi(self, UsersLists):
        UsersLists.setObjectName("UsersLists")
        UsersLists.resize(951, 646)
        UsersLists.setMinimumSize(QtCore.QSize(951, 646))
        UsersLists.setMaximumSize(QtCore.QSize(951, 646))
        self.listWidget_online_users = QtWidgets.QListWidget(UsersLists)
        self.listWidget_online_users.setGeometry(QtCore.QRect(20, 120, 131, 471))
        self.listWidget_online_users.setObjectName("listWidget_online_users")
        self.label_online_users = QtWidgets.QLabel(UsersLists)
        self.label_online_users.setGeometry(QtCore.QRect(20, 90, 131, 21))
        self.label_online_users.setObjectName("label_online_users")
        self.label_friends = QtWidgets.QLabel(UsersLists)
        self.label_friends.setGeometry(QtCore.QRect(180, 90, 101, 21))
        self.label_friends.setObjectName("label_friends")
        self.listWidget_friends = QtWidgets.QListWidget(UsersLists)
        self.listWidget_friends.setGeometry(QtCore.QRect(180, 120, 131, 471))
        self.listWidget_friends.setObjectName("listWidget_friends")
        self.label_username = QtWidgets.QLabel(UsersLists)
        self.label_username.setGeometry(QtCore.QRect(70, 30, 171, 41))
        self.label_username.setObjectName("label_username")
        self.pushButton_fresh_online_users = QtWidgets.QPushButton(UsersLists)
        self.pushButton_fresh_online_users.setGeometry(QtCore.QRect(20, 600, 131, 31))
        self.pushButton_fresh_online_users.setObjectName("pushButton_fresh_online_users")
        self.pushButton_exit = QtWidgets.QPushButton(UsersLists)
        self.pushButton_exit.setGeometry(QtCore.QRect(500, 600, 91, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_send_msg = QtWidgets.QPushButton(UsersLists)
        self.pushButton_send_msg.setGeometry(QtCore.QRect(610, 600, 93, 31))
        self.pushButton_send_msg.setObjectName("pushButton_send_msg")
        self.listWidget_recv_msg = QtWidgets.QListWidget(UsersLists)
        self.listWidget_recv_msg.setGeometry(QtCore.QRect(340, 120, 371, 311))
        self.listWidget_recv_msg.setObjectName("listWidget_recv_msg")
        self.textEdit_msg_edit = QtWidgets.QTextEdit(UsersLists)
        self.textEdit_msg_edit.setGeometry(QtCore.QRect(340, 450, 371, 141))
        self.textEdit_msg_edit.setObjectName("textEdit_msg_edit")
        self.label_show = QtWidgets.QLabel(UsersLists)
        self.label_show.setGeometry(QtCore.QRect(750, 120, 171, 471))
        self.label_show.setObjectName("label_show")
        self.label_user_to = QtWidgets.QLabel(UsersLists)
        self.label_user_to.setGeometry(QtCore.QRect(350, 80, 341, 41))
        self.label_user_to.setObjectName("label_user_to")
        self.pushButton_search = QtWidgets.QPushButton(UsersLists)
        self.pushButton_search.setGeometry(QtCore.QRect(390, 600, 91, 31))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_fresh_friend_list = QtWidgets.QPushButton(UsersLists)
        self.pushButton_fresh_friend_list.setGeometry(QtCore.QRect(180, 600, 131, 31))
        self.pushButton_fresh_friend_list.setObjectName("pushButton_fresh_friend_list")

        self.retranslateUi(UsersLists)
        QtCore.QMetaObject.connectSlotsByName(UsersLists)

    def retranslateUi(self, UsersLists):
        _translate = QtCore.QCoreApplication.translate
        UsersLists.setWindowTitle(_translate("UsersLists", "Form"))
        self.label_online_users.setText(_translate("UsersLists", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">在线用户列表:</span></p></body></html>"))
        self.label_friends.setText(_translate("UsersLists", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">我的好友:</span></p></body></html>"))
        self.label_username.setText(_translate("UsersLists", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">我的用户名</span></p></body></html>"))
        self.pushButton_fresh_online_users.setText(_translate("UsersLists", "刷新在线用户"))
        self.pushButton_exit.setText(_translate("UsersLists", "退出程序"))
        self.pushButton_send_msg.setText(_translate("UsersLists", "发送"))
        self.label_show.setText(_translate("UsersLists", "TextLabel"))
        self.label_user_to.setText(_translate("UsersLists", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">点击左侧用户发送消息</span></p></body></html>"))
        self.pushButton_search.setText(_translate("UsersLists", "查找用户"))
        self.pushButton_fresh_friend_list.setText(_translate("UsersLists", "刷新好友列表"))
