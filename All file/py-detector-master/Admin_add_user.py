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

def add_user_admin(self):
    try:
        path_programm = os.getcwd()
        path = path_programm + "\\userpriv\\"

        id = str(self.di.lineEdit.text())
        name = str(self.di.lineEdit_2.text())
        phone =  str(self.di.lineEdit_3.text())
        email = str(self.di.lineEdit_4.text())
        password = str(self.di.lineEdit_5.text())
        category = str(self.di.comboBox.currentText())

        # Проверяем существуект ли id
        k = True
        with open(path + "Privileges.txt", 'r') as f:
            for lines in f:
                lines = lines.strip().split('^^')
                if str(lines[0]) == id:
                    Error_project.error_14()
                    k = False
                    break

        if k:
            with open(path + "Privileges.txt", 'a') as files:
                files.write(id + "^^" + name + "^^" + phone + "^^" + email + "^^" + password + "^^" + category + "\n")

            Error_project.error_13()

    except:
        Error_project.error_12()

# Просмотр всех пользователей
def see_all_users(self):
    self.di.textEdit.clear()
    path_programm = os.getcwd()
    path = path_programm + "\\userpriv\\"

    with open(path + "Privileges.txt", 'r') as f:
        for lines in f:
            lines = lines.strip().split('^^')
            user_str = "(1)id: " + lines[0] + " (2)Name: " + lines[1] + " (3)Phone: " + lines[2] \
            + " (4)e-mail: " + lines[3] + " (5)Password: " + lines[4] + " (6)Category: "+ lines[5]

            self.di.textEdit.append(user_str)

#Удаление пользователя
def delete_user(self):
    try:
        if self.di.lineEdit.text() != "":
            delet_id = str(self.di.lineEdit.text())
            mass = []
            path_programm = os.getcwd()
            path = path_programm + "\\userpriv\\"
            k = False
            with open(path + "Privileges.txt", 'r') as f:
                for lines in f:
                    line = lines.strip().split('^^')
                    if str(line[0]) == delet_id:
                        k = True
                        pass
                    else:
                        mass.append(lines)
            if k:
                os.remove(path + "Privileges.txt")

                with open(path + "Privileges.txt", 'a') as f:
                    for lines in mass:
                        f.write(lines)
                Error_project.error_17()
        else:
            Error_project.error_15()
    except:
        Error_project.error_16()