# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(621, 488)
        self.textEdit = QtWidgets.QTextEdit(ChatWindow)
        self.textEdit.setGeometry(QtCore.QRect(10, 330, 371, 141))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(ChatWindow)
        self.pushButton.setGeometry(QtCore.QRect(280, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ChatWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(ChatWindow)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 371, 301))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(ChatWindow)
        self.label.setGeometry(QtCore.QRect(420, 50, 151, 381))
        self.label.setObjectName("label")

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "Form"))
        self.pushButton.setText(_translate("ChatWindow", "PushButton"))
        self.pushButton_2.setText(_translate("ChatWindow", "PushButton"))
        self.label.setText(_translate("ChatWindow", "TextLabel"))
