import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def designer_add(self):

    #Настройка размеров
    self.setFixedSize(900, 500)

    # Настройка заднего фона
    oImage = QImage("img\\back\\main.jpg")
    sImage = oImage.scaled(QSize(900, 500))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    temp_shrift = 'SansSerif'
    temp_size_label= 10

    #Настройка qlabel всех

    self.ui.label.setFont(
        QtGui.QFont( temp_shrift,  temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label.setStyleSheet("""
                font: bold italic;
                color:  yellow;
            """)
    self.ui.label_3.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label_3.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)

    self.ui.label_5.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label_5.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)

    self.ui.label_4.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label_4.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)

    self.ui.label_6.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label_6.setStyleSheet("""
                    font: bold italic;
                    color:  yellow;
                """)
    self.ui.label_2.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.ui.label_2.setStyleSheet("""
                        font: bold italic;
                        color:  yellow;
                    """)
    #Настройка кнопок их вида всех
    self.ui.pushButton_5.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ui.pushButton_10.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ui.pushButton_9.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ui.pushButton_8.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ui.pushButton_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ui.pushButton_7.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')