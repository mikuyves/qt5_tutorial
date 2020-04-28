# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.username_Label = QtWidgets.QLabel(Form)
        self.username_Label.setGeometry(QtCore.QRect(27, 52, 60, 16))
        self.username_Label.setObjectName("username_Label")
        self.password_Label = QtWidgets.QLabel(Form)
        self.password_Label.setGeometry(QtCore.QRect(27, 83, 58, 16))
        self.password_Label.setObjectName("password_Label")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(95, 52, 125, 21))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setGeometry(QtCore.QRect(95, 83, 125, 21))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.user_textBrowser = QtWidgets.QTextBrowser(Form)
        self.user_textBrowser.setGeometry(QtCore.QRect(250, 50, 131, 91))
        self.user_textBrowser.setObjectName("user_textBrowser")
        self.login_pushButton = QtWidgets.QPushButton(Form)
        self.login_pushButton.setGeometry(QtCore.QRect(20, 115, 76, 32))
        self.login_pushButton.setObjectName("login_pushButton")
        self.quit_pushButton = QtWidgets.QPushButton(Form)
        self.quit_pushButton.setGeometry(QtCore.QRect(125, 115, 68, 32))
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 160, 91, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.openfile_pushButton = QtWidgets.QPushButton(Form)
        self.openfile_pushButton.setGeometry(QtCore.QRect(260, 160, 113, 32))
        self.openfile_pushButton.setObjectName("openfile_pushButton")
        self.chuang3bed_pushButton = QtWidgets.QPushButton(Form)
        self.chuang3bed_pushButton.setGeometry(QtCore.QRect(40, 221, 61, 51))
        font = QtGui.QFont()
        font.setFamily("YuMincho +36p Kana")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.chuang3bed_pushButton.setFont(font)
        self.chuang3bed_pushButton.setAutoFillBackground(False)
        self.chuang3bed_pushButton.setCheckable(False)
        self.chuang3bed_pushButton.setObjectName("chuang3bed_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Demo"))
        self.username_Label.setText(_translate("Form", "username"))
        self.password_Label.setText(_translate("Form", "password"))
        self.login_pushButton.setText(_translate("Form", "Login"))
        self.quit_pushButton.setText(_translate("Form", "Quit"))
        self.comboBox.setItemText(0, _translate("Form", "Python"))
        self.comboBox.setItemText(1, _translate("Form", "Java"))
        self.comboBox.setItemText(2, _translate("Form", "C++"))
        self.comboBox.setItemText(3, _translate("Form", "Ruby"))
        self.openfile_pushButton.setText(_translate("Form", "Open File"))
        self.chuang3bed_pushButton.setText(_translate("Form", "床"))
