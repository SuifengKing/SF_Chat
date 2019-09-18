# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(381, 321)
        RegisterWindow.setMinimumSize(QtCore.QSize(381, 321))
        RegisterWindow.setMaximumSize(QtCore.QSize(381, 321))
        self.label_title = QtWidgets.QLabel(RegisterWindow)
        self.label_title.setGeometry(QtCore.QRect(30, 30, 321, 31))
        self.label_title.setObjectName("label_title")
        self.label_username = QtWidgets.QLabel(RegisterWindow)
        self.label_username.setGeometry(QtCore.QRect(30, 100, 111, 31))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(RegisterWindow)
        self.label_password.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.label_password.setObjectName("label_password")
        self.label_re_password = QtWidgets.QLabel(RegisterWindow)
        self.label_re_password.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.label_re_password.setObjectName("label_re_password")
        self.lineEdit_username = QtWidgets.QLineEdit(RegisterWindow)
        self.lineEdit_username.setGeometry(QtCore.QRect(170, 100, 181, 31))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(RegisterWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 150, 181, 31))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_re_password = QtWidgets.QLineEdit(RegisterWindow)
        self.lineEdit_re_password.setGeometry(QtCore.QRect(170, 200, 181, 31))
        self.lineEdit_re_password.setObjectName("lineEdit_re_password")
        self.pushButton_register = QtWidgets.QPushButton(RegisterWindow)
        self.pushButton_register.setGeometry(QtCore.QRect(30, 260, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_register.setFont(font)
        self.pushButton_register.setObjectName("pushButton_register")

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "用户注册"))
        self.label_title.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">用户注册</span></p></body></html>"))
        self.label_username.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">用户名:</span></p></body></html>"))
        self.label_password.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">密  码:</span></p></body></html>"))
        self.label_re_password.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">重复密码:</span></p></body></html>"))
        self.pushButton_register.setText(_translate("RegisterWindow", "提交"))
