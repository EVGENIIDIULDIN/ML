import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def enter_designer_window(self):
    oImage = QImage("img\\back\\login.jpg")
    sImage = oImage.scaled(QSize(1027, 722))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    #Настройка всех кнопок
    self.ei.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ei.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')

    #Настройка lineedit

    self.ei.lineEdit.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    self.ei.lineEdit_2.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )