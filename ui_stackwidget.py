# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stackwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(159, -1, 481, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.j5_page = QtWidgets.QWidget()
        self.j5_page.setEnabled(True)
        self.j5_page.setObjectName("j5_page")
        self.title_label = QtWidgets.QLabel(self.j5_page)
        self.title_label.setGeometry(QtCore.QRect(0, 10, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setText("")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.author_label = QtWidgets.QLabel(self.j5_page)
        self.author_label.setGeometry(QtCore.QRect(0, 60, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.author_label.setFont(font)
        self.author_label.setText("")
        self.author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label.setObjectName("author_label")
        self.widget = QtWidgets.QWidget(self.j5_page)
        self.widget.setGeometry(QtCore.QRect(60, 80, 361, 381))
        self.widget.setObjectName("widget")
        self.j5_gridLayout = QtWidgets.QGridLayout(self.widget)
        self.j5_gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.j5_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.j5_gridLayout.setObjectName("j5_gridLayout")
        self.j5_01_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_01_pushButton.setFont(font)
        self.j5_01_pushButton.setText("")
        self.j5_01_pushButton.setObjectName("j5_01_pushButton")
        self.j5_gridLayout.addWidget(self.j5_01_pushButton, 0, 0, 1, 1)
        self.j5_02_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_02_pushButton.setFont(font)
        self.j5_02_pushButton.setText("")
        self.j5_02_pushButton.setObjectName("j5_02_pushButton")
        self.j5_gridLayout.addWidget(self.j5_02_pushButton, 0, 1, 1, 1)
        self.j5_03_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_03_pushButton.setFont(font)
        self.j5_03_pushButton.setText("")
        self.j5_03_pushButton.setObjectName("j5_03_pushButton")
        self.j5_gridLayout.addWidget(self.j5_03_pushButton, 0, 2, 1, 1)
        self.j5_04_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_04_pushButton.setFont(font)
        self.j5_04_pushButton.setText("")
        self.j5_04_pushButton.setObjectName("j5_04_pushButton")
        self.j5_gridLayout.addWidget(self.j5_04_pushButton, 0, 3, 1, 1)
        self.j5_05_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_05_pushButton.setFont(font)
        self.j5_05_pushButton.setText("")
        self.j5_05_pushButton.setObjectName("j5_05_pushButton")
        self.j5_gridLayout.addWidget(self.j5_05_pushButton, 0, 4, 1, 1)
        self.j5_06_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_06_pushButton.setFont(font)
        self.j5_06_pushButton.setText("")
        self.j5_06_pushButton.setCheckable(False)
        self.j5_06_pushButton.setObjectName("j5_06_pushButton")
        self.j5_gridLayout.addWidget(self.j5_06_pushButton, 0, 5, 1, 1)
        self.j5_07_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_07_pushButton.setFont(font)
        self.j5_07_pushButton.setText("")
        self.j5_07_pushButton.setObjectName("j5_07_pushButton")
        self.j5_gridLayout.addWidget(self.j5_07_pushButton, 1, 0, 1, 1)
        self.j5_08_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_08_pushButton.setFont(font)
        self.j5_08_pushButton.setText("")
        self.j5_08_pushButton.setObjectName("j5_08_pushButton")
        self.j5_gridLayout.addWidget(self.j5_08_pushButton, 1, 1, 1, 1)
        self.j5_09_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_09_pushButton.setFont(font)
        self.j5_09_pushButton.setText("")
        self.j5_09_pushButton.setObjectName("j5_09_pushButton")
        self.j5_gridLayout.addWidget(self.j5_09_pushButton, 1, 2, 1, 1)
        self.j5_10_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_10_pushButton.setFont(font)
        self.j5_10_pushButton.setText("")
        self.j5_10_pushButton.setObjectName("j5_10_pushButton")
        self.j5_gridLayout.addWidget(self.j5_10_pushButton, 1, 3, 1, 1)
        self.j5_11_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_11_pushButton.setFont(font)
        self.j5_11_pushButton.setText("")
        self.j5_11_pushButton.setObjectName("j5_11_pushButton")
        self.j5_gridLayout.addWidget(self.j5_11_pushButton, 1, 4, 1, 1)
        self.j5_12_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_12_pushButton.setFont(font)
        self.j5_12_pushButton.setText("")
        self.j5_12_pushButton.setObjectName("j5_12_pushButton")
        self.j5_gridLayout.addWidget(self.j5_12_pushButton, 1, 5, 1, 1)
        self.j5_13_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_13_pushButton.setFont(font)
        self.j5_13_pushButton.setText("")
        self.j5_13_pushButton.setObjectName("j5_13_pushButton")
        self.j5_gridLayout.addWidget(self.j5_13_pushButton, 2, 0, 1, 1)
        self.j5_14_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_14_pushButton.setFont(font)
        self.j5_14_pushButton.setText("")
        self.j5_14_pushButton.setObjectName("j5_14_pushButton")
        self.j5_gridLayout.addWidget(self.j5_14_pushButton, 2, 1, 1, 1)
        self.j5_15_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_15_pushButton.setFont(font)
        self.j5_15_pushButton.setText("")
        self.j5_15_pushButton.setObjectName("j5_15_pushButton")
        self.j5_gridLayout.addWidget(self.j5_15_pushButton, 2, 2, 1, 1)
        self.j5_16_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_16_pushButton.setFont(font)
        self.j5_16_pushButton.setText("")
        self.j5_16_pushButton.setObjectName("j5_16_pushButton")
        self.j5_gridLayout.addWidget(self.j5_16_pushButton, 2, 3, 1, 1)
        self.j5_17_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_17_pushButton.setFont(font)
        self.j5_17_pushButton.setText("")
        self.j5_17_pushButton.setObjectName("j5_17_pushButton")
        self.j5_gridLayout.addWidget(self.j5_17_pushButton, 2, 4, 1, 1)
        self.j5_18_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_18_pushButton.setFont(font)
        self.j5_18_pushButton.setText("")
        self.j5_18_pushButton.setObjectName("j5_18_pushButton")
        self.j5_gridLayout.addWidget(self.j5_18_pushButton, 2, 5, 1, 1)
        self.j5_19_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_19_pushButton.setFont(font)
        self.j5_19_pushButton.setText("")
        self.j5_19_pushButton.setObjectName("j5_19_pushButton")
        self.j5_gridLayout.addWidget(self.j5_19_pushButton, 3, 0, 1, 1)
        self.j5_20_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_20_pushButton.setFont(font)
        self.j5_20_pushButton.setText("")
        self.j5_20_pushButton.setObjectName("j5_20_pushButton")
        self.j5_gridLayout.addWidget(self.j5_20_pushButton, 3, 1, 1, 1)
        self.j5_21_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_21_pushButton.setFont(font)
        self.j5_21_pushButton.setText("")
        self.j5_21_pushButton.setObjectName("j5_21_pushButton")
        self.j5_gridLayout.addWidget(self.j5_21_pushButton, 3, 2, 1, 1)
        self.j5_22_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_22_pushButton.setFont(font)
        self.j5_22_pushButton.setText("")
        self.j5_22_pushButton.setObjectName("j5_22_pushButton")
        self.j5_gridLayout.addWidget(self.j5_22_pushButton, 3, 3, 1, 1)
        self.j5_23_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_23_pushButton.setFont(font)
        self.j5_23_pushButton.setText("")
        self.j5_23_pushButton.setObjectName("j5_23_pushButton")
        self.j5_gridLayout.addWidget(self.j5_23_pushButton, 3, 4, 1, 1)
        self.j5_24_pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.j5_24_pushButton.setFont(font)
        self.j5_24_pushButton.setText("")
        self.j5_24_pushButton.setObjectName("j5_24_pushButton")
        self.j5_gridLayout.addWidget(self.j5_24_pushButton, 3, 5, 1, 1)
        self.stackedWidget.addWidget(self.j5_page)
        self.j7_page = QtWidgets.QWidget()
        self.j7_page.setObjectName("j7_page")
        self.label_2 = QtWidgets.QLabel(self.j7_page)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 59, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.j7_page)
        self.l5_page = QtWidgets.QWidget()
        self.l5_page.setObjectName("l5_page")
        self.label_3 = QtWidgets.QLabel(self.l5_page)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 59, 16))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.l5_page)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.chs_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.chs_checkBox.setGeometry(QtCore.QRect(30, 390, 81, 41))
        self.chs_checkBox.setObjectName("chs_checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "七言律诗"))
        self.label_3.setText(_translate("MainWindow", "五言律诗"))
        self.comboBox.setItemText(0, _translate("MainWindow", "登鸛雀樓"))
        self.comboBox.setItemText(1, _translate("MainWindow", "靜夜思"))
        self.chs_checkBox.setText(_translate("MainWindow", "简体版本"))