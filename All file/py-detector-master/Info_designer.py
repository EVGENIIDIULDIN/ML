import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def info_designer(self):
    # Настройка выхода
    exitAction4 = QAction(QIcon('exit.png'), 'Exit', self)
    exitAction4.setShortcut('Ctrl+U')
    exitAction4.triggered.connect(self.close)

    self.toolbar = self.addToolBar('Info')
    self.toolbar.addAction(exitAction4)

    # Настройка фона

    oImage = QImage("backadmin.jpg")
    sImage = oImage.scaled(QSize(801, 775))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(sImage))
    self.setPalette(palette)

    #Настройка button

    self.ti.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: dark; font : 10pt ;}')

    # Настройка textedit
    self.ti.textEdit.setStyleSheet('background-color: rgb(33, 33, 33);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(255, 255, 255);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )

    #Настройка combobox
    self.ti.comboBox.setStyleSheet('background-color: rgb(0, 191, 255);'
                                   'border-color: rgb(18, 18, 18);'
                                   'color: rgb(0, 0, 0);'
                                   'font: bold italic 14pt "Times New Roman";'
                                   )
