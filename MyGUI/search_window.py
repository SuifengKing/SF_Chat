# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(680, 470)
        self.lineEdit_keyword = QtWidgets.QLineEdit(SearchWindow)
        self.lineEdit_keyword.setGeometry(QtCore.QRect(30, 30, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_keyword.setFont(font)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.listWidget_result = QtWidgets.QListWidget(SearchWindow)
        self.listWidget_result.setGeometry(QtCore.QRect(30, 100, 611, 301))
        self.listWidget_result.setObjectName("listWidget_result")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_result.addItem(item)
        self.pushButton_search = QtWidgets.QPushButton(SearchWindow)
        self.pushButton_search.setGeometry(QtCore.QRect(480, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_tip = QtWidgets.QLabel(SearchWindow)
        self.label_tip.setGeometry(QtCore.QRect(30, 420, 611, 31))
        self.label_tip.setObjectName("label_tip")

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "查找"))
        self.lineEdit_keyword.setPlaceholderText(_translate("SearchWindow", "请输入用户名/昵称(当前仅支持用户名!!!)"))
        __sortingEnabled = self.listWidget_result.isSortingEnabled()
        self.listWidget_result.setSortingEnabled(False)
        item = self.listWidget_result.item(0)
        item.setText(_translate("SearchWindow", "此处显示结果"))
        self.listWidget_result.setSortingEnabled(__sortingEnabled)
        self.pushButton_search.setText(_translate("SearchWindow", "查找"))
        self.label_tip.setText(_translate("SearchWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">双击用户添加好友</span></p></body></html>"))
