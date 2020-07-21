import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



def open_info(self):
    if self.ti.comboBox.currentIndex() == 0:
        self.ti.textEdit.setText(
            "В данной программе мы разработали многопоточную систему обработки конфиденциальных данных с применением нейронных сетей")
        self.ti.textEdit.append(
            "В программе содержится система для автоматического добавления пользователей, а так же в ручную")
        self.ti.textEdit.append("Вы так же можете из общей базы данных выбрать пользователей, которые нужны вам для тренировки нейронной сети"
            )
        self.ti.textEdit.append("Дополнительные функции представлены в виде настройки камеры, параметров, и info"
            )
        self.ti.textEdit.append("В данной программе реализован режим администрирования"
                                )
        self.ti.textEdit.append("Интерфейс интуитивно понятен, следуйте по шагам (1) --> (5)"
                               )
