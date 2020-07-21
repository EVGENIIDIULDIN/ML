import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def designer_user_add(self):

    oImage = QImage("img\\back\\main.jpg")
    sImage = oImage.scaled(QSize(858, 490))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    temp_shrift = 'SansSerif'
    temp_size_label = 8

    # Настройка qlabel всех

    self.ai.label_3.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ai.label_3.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)

    self.ai.label_4.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ai.label_4.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.ai.label_5.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ai.label_5 .setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)

    self.ai.label_6.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ai.label_6.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)


    # Настройка всех значений кнопок
    self.ai.pushButton_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ai.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ai.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ai.pushButton_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')

    #Настройка combobox
    self.ai.comboBox.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    #Настройка lineedit
    self.ai.lineEdit.setStyleSheet('background-color: rgb(0, 191, 255);'
                                      'border-color: rgb(18, 18, 18);'
                                      'color: rgb(0, 0, 0);'
                                      'font: bold italic 14pt "Times New Roman";'
                                      )
    self.ai.lineEdit_3.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    self.ai.lineEdit_4.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

