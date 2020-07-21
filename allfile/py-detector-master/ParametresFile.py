import sys
import cv2
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from FirstWindow import Ui_MainWindow
from ThirdWindow import Ui_MainWindow3
from Autom_add_Window import Ui_MainWindow2
from HelpWindow import Ui_MainWindow4

from TestCamera import test_camera
from Error_Class import Error_project
from Start_add_user import autom_start_add

#Задаём параметры
def parametres_add(self):
    if self.ci.lineEdit_4.text() != "":
        self.dir_path = self.ci.lineEdit_4.text()

    if self.ci.lineEdit_5.text() != "":
        self.face_minNeighbours = int(self.ci.lineEdit_5.text())

    if self.ci.lineEdit_7.text() != "":
        self.eye_scaleFactor = float(self.ci.lineEdit_7.text())

    if self.ci.lineEdit_8.text() != "":
        self.eye_minNeighbours = int(self.ci.lineEdit_8.text())

    if self.ci.lineEdit_9.text() != "":
        self.eye_scaleFactor = float(self.ci.lineEdit_9.text())

    if self.ci.lineEdit_11.text() != "":
        self.luck_minNeighbours = int(self.ci.lineEdit_11.text())

    if self.ci.lineEdit_12.text() != "":
        self.luck_scaleFactor = float(self.ci.lineEdit_12.text())

    if self.ci.lineEdit.text() != "":
        self.face_detected = str(self.ci.lineEdit.text())

    if self.ci.lineEdit_2.text() != "":
        self.eye_detected = str(self.ci.lineEdit_2.text())

    if self.ci.lineEdit_3.text() != "":
        self.luck_detected = str(self.ci.lineEdit_3.text())

#Возвращаем стандартные параметры
def return_standart(self):
    self.path_programm = os.getcwd()
    self.dir_path = self.path_programm + f"\\dataset\\user."
    self.neiron_save = self.path_programm + f'\\trainer\\'

    # Настройки haarcascade
    self.face_detected = self.path_programm + f"\\xml\\haarcascade_frontalface_default.xml"
    self.eye_detected = self.path_programm + f"\\xml\\haarcascade_eye.xml"
    self.luck_detected = self.path_programm + f"\\xml\\haarcascade_smile.xml"

    # Настройки для лица
    self.face_minNeighbours = 5
    self.face_scaleFactor = 1.3

    # Настройки для глаз
    self.eye_minNeighbours = 5
    self.eye_scaleFactor = 1.5
    self.eye_minSize = (5, 5)

    # Натсройка улыбки

    self.luck_minNeighbours = 15
    self.luck_scaleFactor = 1.5
    self.luck_minSize = (25, 25)

def image_parametres(self):
    self.ci.lineEdit_4.setText(str(self.dir_path))
    self.ci.lineEdit_15.setText(str(self.neiron_save))
    self.ci.lineEdit_14.setText(str(self.path_id))

    #Настрйока параметров
    self.ci.lineEdit_5.setText(str(self.face_minNeighbours))
    self.ci.lineEdit_7.setText(str(self.face_scaleFactor))
    self.ci.lineEdit_8.setText(str(self.eye_minNeighbours))
    self.ci.lineEdit_9.setText(str(self.eye_scaleFactor))
    self.ci.lineEdit_11.setText(str(self.luck_minNeighbours))
    self.ci.lineEdit_12.setText(str(self.luck_scaleFactor))

    self.ci.lineEdit.setText(str(self.face_detected))
    self.ci.lineEdit_2.setText(str(self.eye_detected))
    self.ci.lineEdit_3.setText(str(self.luck_detected))
