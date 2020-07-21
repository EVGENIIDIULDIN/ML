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




def designer_user_change(self):
    self.setFixedSize(901, 457)

    oImage = QImage("img\\back\\main.jpg")
    sImage = oImage.scaled(QSize(901, 457))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    # Дизайн всех кнопок
    self.ki.pushButton_3.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ki.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ki.pushButton_4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')
    self.ki.pushButton_5.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')


    #Настройка linedit
    self.ki.lineEdit.setStyleSheet('background-color: rgb(0, 191, 255);'
                                      'border-color: rgb(18, 18, 18);'
                                      'color: rgb(0, 0, 0);'
                                      'font: bold italic 14pt "Times New Roman";'
                                      )
    #Настрйока textedit
    self.ki.textEdit.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    self.ki.textEdit_2.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";')
    #Настрйка выхода
    exitAction4 = QAction(QIcon('img\\icons\\exit.jpg'), 'Exit', self)
    exitAction4.setShortcut('Ctrl+U')
    exitAction4.triggered.connect(self.close)

    exitAction1 = QAction(QIcon('img\\icons\\clear.jpg'), 'Clear', self)
    exitAction1.setShortcut('Ctrl+G')
    exitAction1.triggered.connect(self.id_mass.clear)



    self.toolbar = self.addToolBar('Info')
    self.toolbar.addAction(exitAction4)
    self.toolbar.addAction(exitAction1)

