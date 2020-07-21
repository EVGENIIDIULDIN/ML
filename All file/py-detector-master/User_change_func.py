import sys
import cv2
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Error_Class import Error_project

# Выводим пользователей в окне



def user_change_func(self, helpwindow):
    self.ki.textEdit.clear()
    paths = helpwindow.path_id + "IDCategoryName.txt"


    with open(paths, 'r') as file:
        helpwindow.step_mass = []
        for line in file:
            line = line.strip().split('^^')
            lines_add = "(1)id: " + line[0] + " (2)name: " + line[1] + " (3)category: " + line[2]
            helpwindow.step_mass.append(int(line[0]))
            self.ki.textEdit.append(lines_add)

# Ищем пользователей
def seek_user(self, helpwindow, isbool=True, step_plus = True):
    try:
        helpwindow.step_mass = sorted(helpwindow.step_mass)
        len_mass_ind = len(helpwindow.step_mass)

        if int(self.ki.lineEdit.text()) in helpwindow.step_mass:

            # Просто нажали кнопку выбрать id
            if isbool:
                    id_us = int(self.ki.lineEdit.text())

            elif not isbool:
                # шаг вперёд
                index_1 = helpwindow.step_mass.index(int(self.ki.lineEdit.text()))

                if step_plus == True:
                    if index_1 + 1 < len_mass_ind:
                        id_us = helpwindow.step_mass[int(index_1) + 1]
                        # Меняем значение на +1 в lineedit
                        self.ki.lineEdit.setText(str(helpwindow.step_mass[index_1 + 1]))

                elif step_plus == False:
                    if int(self.ki.lineEdit.text()) > 0:
                        id_us = helpwindow.step_mass[int(index_1) - 1]
                        self.ki.lineEdit.setText(str(helpwindow.step_mass[int(index_1) - 1]))
                    else:
                        Error_project.error_23()

            helpwindow.path_programm = os.getcwd()
            helpwindow.dir_path = helpwindow.path_programm + "\dataset"

            # Путь до файла с фото
            path = helpwindow.dir_path

            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

            for imagePath in imagePaths:
                # PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
                # img_numpy = np.array(PIL_img, 'uint8')

                id = int(os.path.split(imagePath)[-1].split(".")[1])

                if id == id_us:
                    self.id_now = id
                    self.ki.label.setPixmap(QtGui.QPixmap(imagePath))
                    break
        else:
            Error_project.error_24()
    except:
        Error_project.error_19()


# Пошаговый шага вперёд
def step_seek_user(self, helpwindow):
    seek_user(self, helpwindow, False, True)

# Пошаговый режим шага назад
def step_last_end(self, helpwindow):
    seek_user(self, helpwindow, False, False)