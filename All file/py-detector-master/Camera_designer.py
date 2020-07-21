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

from Error_Class import  Error_project

def camera_designer_new(self):
    #настройка размеров
    self.setFixedSize(901, 457)

    #Настрйока заднего фона
    oImage = QImage("img\\back\\main.jpg")
    sImage = oImage.scaled(QSize(901, 457))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    # Настрйка выхода
    exitAction4 = QAction(QIcon('img\\icons\\exit.jpg'), 'Exit', self)
    exitAction4.setShortcut('Ctrl+U')
    exitAction4.triggered.connect(self.close)

    self.toolbar = self.addToolBar('Info')
    self.toolbar.addAction(exitAction4)

    #Настройка картинок камер
    self.pi.label.setPixmap(QtGui.QPixmap("img\\icons\\cam1.jpg"))
    self.pi.label_2.setPixmap(QtGui.QPixmap("img\\icons\\cam2.jpg"))
    self.pi.label_3.setPixmap(QtGui.QPixmap("img\\icons\\cam3.jpg"))
    self.pi.label_4.setPixmap(QtGui.QPixmap("img\\icons\\cam4.jpg"))

    #Настройки кнопок
    self.pi.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')

    #Настройка checkbox
    style = 'border-color: rgb(18, 18, 18);'+'color: white;'+'font: bold italic 14pt "Times New Roman";'
    self.pi.checkBox.setStyleSheet(style)
    self.pi.checkBox_4.setStyleSheet(style)
    self.pi.checkBox_2.setStyleSheet(style)
    self.pi.checkBox_3.setStyleSheet(style)