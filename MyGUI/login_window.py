# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(446, 291)
        LoginWindow.setMinimumSize(QtCore.QSize(446, 291))
        LoginWindow.setMaximumSize(QtCore.QSize(446, 291))
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 20, 361, 31))
        self.label_name.setObjectName("label_name")
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(100, 200, 101, 31))
        self.pushButton_register.setObjectName("pushButton_register")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(250, 200, 101, 31))
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(160, 80, 221, 31))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(160, 130, 221, 31))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(70, 80, 71, 31))
        self.label_password.setObjectName("label_password")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(70, 140, 71, 21))
        self.label_username.setObjectName("label_username")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "登录"))
        LoginWindow.setToolTip(_translate("LoginWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_name.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">名字还没想好……</span></p></body></html>"))
        self.pushButton_register.setText(_translate("LoginWindow", "注册"))
        self.pushButton_login.setText(_translate("LoginWindow", "登录"))
        self.label_password.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">用户名:</span></p></body></html>"))
        self.label_username.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">密 码:</span></p></body></html>"))
