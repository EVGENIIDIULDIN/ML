import sys
import cv2
import os
import shutil
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *




def neiron_change_designer(self):
    # Настройка размеров
    self.setFixedSize(800, 600)

    oImage = QImage("img\\back\\main.jpg")
    sImage = oImage.scaled(QSize(800, 600))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)


    # Настрйока textedit
    self.nni.textEdit.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    # Настрйока textedit
    self.nni.textEdit_2.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    # Настрйока textedit
    self.nni.textEdit_3.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    # Настрйока textedit
    self.nni.textEdit_4.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
    # Настрйока textedit
    self.nni.textEdit_5.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    temp_shrift = 'SansSerif'
    temp_size_label = 10

    # Настройка qlabel всех

    self.nni.label.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.nni.label.setStyleSheet("""
                   font: bold italic;
                   color:  yellow;
               """)
    temp_shrift = 'SansSerif'
    temp_size_label = 10

    # Настройка qlabel всех

    self.nni.label_2.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.nni.label_2.setStyleSheet("""
                      font: bold italic;
                      color:  yellow;
                  """)
    temp_shrift = 'SansSerif'
    temp_size_label = 10

    self.nni.label_3.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.nni.label_3.setStyleSheet("""
                      font: bold italic;
                      color:  yellow;
                  """)
    temp_shrift = 'SansSerif'
    temp_size_label = 10

    self.nni.label_4.setFont(
        QtGui.QFont(temp_shrift, temp_size_label)
    )  # Изменение шрифта и размера
    # Настройка цвета шагов

    self.nni.label_4.setStyleSheet("""
                      font: bold italic;
                      color:  yellow;
                  """)
    temp_shrift = 'SansSerif'
    temp_size_label = 10

    self.nni.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
