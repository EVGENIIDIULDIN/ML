import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def designer_helpwindow(self):
    #Настройка размера
    self.setFixedSize(580, 510)


    oImage = QImage("img\\back\\admin.jpg")
    sImage = oImage.scaled(QSize(580, 510))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)


    style = 'color:  white;'

    self.ci.label_19.setStyleSheet(style)
    self.ci.label_20.setStyleSheet(style)
    self.ci.label_3.setStyleSheet(style)
    self.ci.label_4.setStyleSheet(style)
    self.ci.label_5.setStyleSheet(style)
    self.ci.label_6.setStyleSheet(style)
    self.ci.label_7.setStyleSheet(style)
    self.ci.label_9.setStyleSheet(style)

    # Настройка выхода

    exitAction4 = QAction(QIcon('img\\icons\\exit.jpg'), 'Exit', self)
    exitAction4.setShortcut('Ctrl+U')
    exitAction4.triggered.connect(self.close)

    self.toolbar = self.addToolBar('Info')
    self.toolbar.addAction(exitAction4)