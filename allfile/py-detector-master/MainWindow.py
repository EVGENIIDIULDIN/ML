# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\TMP\FSO_bin\DesignerFile\MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 80, 221, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 80, 221, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 320, 221, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(610, 200, 221, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 61, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 100, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 71, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 210, 71, 51))
        self.label_4.setObjectName("label_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 320, 221, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 330, 61, 51))
        self.label_5.setObjectName("label_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 200, 221, 71))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 330, 71, 51))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Модуль распознавания субъектов доступа"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить людей вручную"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить людей автоматически"))
        self.pushButton_7.setText(_translate("MainWindow", "Старт"))
        self.pushButton_8.setText(_translate("MainWindow", "Обучить нейронную сеть"))
        self.label.setText(_translate("MainWindow", "Шаг №1"))
        self.label_2.setText(_translate("MainWindow", "Или"))
        self.label_3.setText(_translate("MainWindow", "Шаг №2"))
        self.label_4.setText(_translate("MainWindow", "Шаг №3"))
        self.pushButton_9.setText(_translate("MainWindow", "Выбрать файл нейронной сети"))
        self.label_5.setText(_translate("MainWindow", "Шаг №4"))
        self.pushButton_10.setText(_translate("MainWindow", "Выбрать людей "))
        self.label_6.setText(_translate("MainWindow", "Шаг №5"))
        self.action123.setText(_translate("MainWindow", "123"))
        self.action123.setToolTip(_translate("MainWindow", "сообщение"))