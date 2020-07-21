import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



def add_admin_designer(self):

    #Размер окна
    self.setFixedSize(1027, 722)

    oImage = QImage("backadmin.jpg")
    sImage = oImage.scaled(QSize(1027, 722))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)



    temp_shrift = 'SansSerif'
    temp_size_label = 8

    # Настройка всех label

    self.di.label_2.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label_2.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)

    self.di.label_3.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label_3.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.di.label_4.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label_4.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.di.label_5.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label_5.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.di.label_6.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label_6.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.di.label.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера

    self.di.label.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    #Настройка всех кнопок
    self.di.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.di.pushButton_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.di.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')

    #Настройка цвета textedit
    self.di.textEdit.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    # Настрйока выхода
    exitAction4 = QAction(QIcon('exit.png'), 'Exit', self)
    exitAction4.setShortcut('Ctrl+U')
    exitAction4.triggered.connect(self.close)

    self.toolbar = self.addToolBar('Info')
    self.toolbar.addAction(exitAction4)

    #Дизайн lineedit

    self.di.lineEdit.setStyleSheet('background-color: rgb(0, 191, 255);'
                                     'border-color: rgb(18, 18, 18);'
                                     'color: rgb(0, 0, 0);'
                                     'font: bold italic 14pt "Times New Roman";'
                                     )

    self.di.lineEdit_2.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    self.di.lineEdit_3.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    self.di.lineEdit_4.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    self.di.lineEdit_5.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    # Настройка combobox
    self.di.comboBox.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
