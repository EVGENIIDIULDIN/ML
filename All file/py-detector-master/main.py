import sys
import cv2
import os
import shutil
import datetime
import sqlite3
# import pkg_resources.py2_warn

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from MainWindow import Ui_MainWindow
from ThirdWindow import Ui_MainWindow3
from Autom_add_Window import Ui_MainWindow2
from HelpWindow import Ui_MainWindow4
from EnterWindiw import Ui_MainWindow5
from AdministrationWindow import Ui_MainWindow6
from InfoWindow import Ui_MainWindow7
from UserChangeWindow import Ui_MainWindow8
from CameraParamWindow import Ui_MainWindow9
from NeironChange import Ui_MainWindow11

from Admin_add_user import add_user_admin, see_all_users, delete_user
from TestCamera import test_camera
from Error_Class import Error_project
from Start_add_user import autom_start_add
from ParametresFile import parametres_add, return_standart, image_parametres
from NeronTraining import start_train
from StartTestNeiron import start_test_neirons, pre_start_train
from ColorMainWindow import designer_add
from Color_add_Window import designer_user_add
from Admin_add_designer import add_admin_designer
from Enter_designer_window import enter_designer_window
from HelpWindow_designer import designer_helpwindow
from Info_designer import info_designer
from OpenInfo_Info import open_info
from User_change_func import user_change_func, seek_user, step_seek_user, step_last_end
from designer_user_change import designer_user_change
from Camera_designer import camera_designer_new
from NeironDesignerChange import  neiron_change_designer


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

        # Обработка нажатия кнопок
        # self.ui.pushButton.clicked.connect(self.show_help)
        # self.ui.pushButton_2.clicked.connect(self.camera_test)
        # self.ui.pushButton_3.clicked.connect(self.open_customization)
        self.ui.pushButton_4.clicked.connect(self.open_hand_dir)
        self.ui.pushButton_5.clicked.connect(self.automatically_add_user)
        # self.ui.pushButton_6.clicked.connect(self.close)
        self.ui.pushButton_7.clicked.connect(self.start_test_neiron)
        self.ui.pushButton_8.clicked.connect(self.start_training_neiron)
        self.ui.pushButton_9.clicked.connect(self.neiron_change)
        self.ui.pushButton_10.clicked.connect(self.open_change_window)
        # self.ui.pushButton_4.setIcon(QIcon('gg.jpg'))
        # self.ui.pushButton_4.setIconSize(QSize(200, 100))

        # Настройка дизайна главного окна
        designer_add(self)

    # Настройка menubar и toolbar
    def initUI(self):
        # Открываем параметры
        exitAction = QAction(QIcon('img\\icons\\param.jpg'), '&Открыть', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Open Parametres')
        exitAction.triggered.connect(self.open_customization)

        # Открываем привелегии
        # exitAction1 = QAction(QIcon('img\\icons\\privil.png'), '&Admins', self)
        # exitAction1.setShortcut('Ctrl+P')
        # exitAction1.setStatusTip('Exit applicationssss')
        # exitAction1.triggered.connect(admins.show)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Параметры')
        # fileMenus = menubar.addMenu('&Администрирование')
        fileMenu.addAction(exitAction)
        # fileMenus.addAction(exitAction1)

        # Работаем с toolbar
        exitAction2 = QAction(QIcon('img\\icons\\param.jpg'), 'Info', self)
        exitAction2.setShortcut('Ctrl+W')
        exitAction2.triggered.connect(self.open_customization)

        # Настройка камеры

        exitAction3 = QAction(QIcon('img\\icons\\cam1.jpg'), 'Camera', self)
        exitAction3.setShortcut('Ctrl+R')
        exitAction3.triggered.connect(self.camera_test)

        # Настройка выхода
        exitAction5 = QAction(QIcon('img\\icons\\saveicon.jpg'), 'SaveCam', self)
        exitAction5.setShortcut('Ctrl+U')
        exitAction5.triggered.connect(self.open_save_cam)

        # Настройка выхода
        exitAction4 = QAction(QIcon('img\\icons\\exit.jpg'), 'Exit', self)
        exitAction4.setShortcut('Ctrl+U')
        exitAction4.triggered.connect(self.close)

        self.toolbar = self.addToolBar('Info')
        self.toolbar.addAction(exitAction2)
        self.toolbar.addAction(exitAction3)
        self.toolbar.addAction(exitAction5)
        self.toolbar.addAction(exitAction4)

    # Метод для показа справки
    def show_help(self):
        thirdapp.show()

    # Метод естирования работы камеры
    def camera_test(self):
        test_camera(self, helpwindow)

    # Открываем окно автоматического добавления пользователей
    def automatically_add_user(self):
        autom_add.show()

    # Открываем окно настроек
    def open_customization(self):
        helpwindow.show()

    # Открываем директорию для ручного заполнения
    def open_hand_dir(self):
        self.path_programm = os.getcwd()
        self.dir_path = self.path_programm + "\dataset\ "

        os.system(f'explorer {self.dir_path}')

    # Открыть окно выбора людей
    def open_change_window(self):
        userchange.show()
        user_change_func(userchange, helpwindow)

    # Выбираем файл нейронной сети
    def neiron_change(self):
        neirons.nni.textEdit_2.clear()
        neirons.see_all_neirons()
        neirons.show()

    # Начинаем тренировать нейронную сеть
    def start_training_neiron(self):

        text, ok = QInputDialog.getText(self, 'Название',
                                        'Название нейронной сети:')
        if not ok:
            pass
        else:
            if text == "":
                Error_project.error_25()
                date = datetime.datetime.today()
                date = date.strftime('%d-%m-%Y %H:%M')
                start_train(self, helpwindow, userchange, date, flags=1)
            else:
                if len(text) > 120:
                    text =  text[0:120]
                    Error_project.error_25()
                start_train(self, helpwindow, userchange, text, flags=0)

    # Проверка нейронной сети
    def start_test_neiron(self):
        try:
            message = 'Хотите открыть директорию сохранения?'
            reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:

                self.path_programm = os.getcwd()
                self.dir_path = self.path_programm + "\\DETECTED\\"
                os.system(f'explorer {self.dir_path}')

                #Начинаем тест нейронной сети
                pre_start_train(self, helpwindow, cameraparam, neirons)
            else:
                pre_start_train(self, helpwindow, cameraparam, neirons)

        # start_test_neirons(self, helpwindow)
        except:
            Error_project.error_30()

    #Открываем директорию сохранения камер
    def open_save_cam(self):
        self.path_programm = os.getcwd()
        self.dir_path = self.path_programm + "\\DETECTED\\ "
        os.system(f'explorer {self.dir_path}')


# Окно справки
class ThirdWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ti = Ui_MainWindow7()
        self.ti.setupUi(self)

        self.setFixedSize(801, 775)
        # Настройка дизайна
        info_designer(self)

        # Настройка combobox
        self.ti.comboBox.addItem("Как использовать")

        # Настройка textedit
        self.ti.textEdit.setReadOnly(True)

        # Настройка кнопок
        self.ti.pushButton.clicked.connect(self.open_info)

    def open_info(self):
        open_info(self)


# Класс автоматического добавления пользователей
class Autom_add_user(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ai = Ui_MainWindow2() #каркас формы
        self.ai.setupUi(self)

        # Настройка открытия
        exitAction3 = QAction(QIcon('img\\icons\\folder.jpg'), '&UserFile', self)
        exitAction3.setShortcut('Ctrl+L')
        exitAction3.setStatusTip('Open ID')
        exitAction3.triggered.connect(self.open_user_dir)

        # Настройка очистки
        exitAction2 = QAction(QIcon('img\\icons\\folder.jpg'), '&Clear', self)
        exitAction2.setShortcut('Ctrl+L')
        exitAction2.setStatusTip('Open ID')
        exitAction2.triggered.connect(self.clear_file_id)

        # Натсройка menubar
        exitAction = QAction(QIcon('img\\icons\\param.jpg'), '&Open', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Open Parametres')
        exitAction.triggered.connect(application.open_customization)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Parametres')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction2)
        fileMenu.addAction(exitAction3)

        # Создание дизайна окна
        designer_user_add(self)

        # Заполнение combobox
        self.ai.comboBox.addItem("usually")
        self.ai.comboBox.addItem("verifiable")
        self.ai.comboBox.addItem("important")

        # Обработка нажатий на кнопки

        self.ai.pushButton_3.clicked.connect(self.close)
        self.ai.pushButton.clicked.connect(self.start_add_user)
        self.ai.pushButton_2.clicked.connect(self.open_work_dir)
        self.ai.pushButton_4.clicked.connect(self.clear_dir)

    def start_add_user(self):
        if self.ai.lineEdit.text() != "" and self.ai.lineEdit_3.text() != "" and self.ai.lineEdit_4.text() != "":

            try:
                self.id_user = int(self.ai.lineEdit.text())
                self.freim = int(self.ai.lineEdit_3.text())

                # Переходим к добавлению  пользователей
                autom_start_add(self, helpwindow)
                with open(helpwindow.path_id + "IDCategoryName.txt", 'a') as files:
                    files.write(str(self.ai.lineEdit.text()) + "^^" + str(self.ai.lineEdit_4.text()) + "^^" + str(
                        self.ai.comboBox.currentText()) + "\n")

            except:
                Error_project.error_2()

        else:
            Error_project.error_1()

    # Открываем директорию
    def open_work_dir(self):
        self.path_programm = os.getcwd()
        self.dir_path = self.path_programm + "\dataset\ "
        os.system(f'explorer {self.dir_path}')

    # Очищаем директорию фото
    def clear_dir(self):

        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            path_programm = os.getcwd()
            dir_path = path_programm + "\\dataset\\"
            dirpath = dir_path
            for filename in os.listdir(dirpath):
                filepath = os.path.join(dirpath, filename)
                try:
                    shutil.rmtree(filepath)
                except OSError:
                    os.remove(filepath)
            Error_project.error_9()

        # Очищаем файл с именем
        else:
            pass

    def clear_file_id(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            with open(helpwindow.path_id + "IDCategoryName.txt", 'w') as files:
                files.write("")
            Error_project.error_31()

        else:
            pass


    # Открываем файл userid
    def open_user_dir(self):
        self.path_programm = os.getcwd()
        self.dir_path = self.path_programm + "\\userid\\IDCategoryName.txt "
        os.system(f'explorer {self.dir_path}')

#Класс настроек
class HelpWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ci = Ui_MainWindow4()
        self.ci.setupUi(self)
        self.ci.lineEdit_4.setReadOnly(True)

        #Используем когда считаем пользователей в ChangeWindow
        self.user_count = 0
        self.step_mass = []

        # Настройка кнопок при нажатии

        # self.ci.pushButton_2.clicked.connect(self.close)
        self.ci.pushButton_3.clicked.connect(self.change_save)
        self.ci.pushButton.clicked.connect(self.return_standart_param)
        self.ci.pushButton_4.clicked.connect(self.camera_param)

        # Создайм дизайн
        designer_helpwindow(self)

        # Переменные путей в настройках

        # Показывает где лежит исполняемый файл

        self.path_programm = os.getcwd()
        self.dir_path = self.path_programm + f"\\dataset\\user."
        self.neiron_save = self.path_programm + f'\\trainer\\'
        self.path_id = self.path_programm + f"\\userid\\"

        # Настройки haarcascade
        self.face_detected = self.path_programm + "\\xml\\haarcascade_frontalface_default.xml"
        self.eye_detected = self.path_programm + "\\xml\\haarcascade_eye.xml"
        self.luck_detected = self.path_programm + "\\xml\\haarcascade_smile.xml"

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
        image_parametres(self)

        #Настрйока lineedit
        self.ci.lineEdit_14.setReadOnly(True)
        self.ci.lineEdit_15.setReadOnly(True)
        self.ci.lineEdit.setReadOnly(True)
        self.ci.lineEdit_2.setReadOnly(True)
        self.ci.lineEdit_3.setReadOnly(True)



    def change_save(self):

        try:
            parametres_add(self)
            Error_project.error_6()
            image_parametres(self)
        except:
            Error_project.error_5()

    # Возвращаем стандартные настройки
    def return_standart_param(self):
        return_standart(self)
        image_parametres(self)

    def camera_param(self):
        cameraparam.show()


# Окно входа в программу
class EnterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ei = Ui_MainWindow5()
        self.ei.setupUi(self)

        # Изменяем размеры окна
        self.setFixedSize(752, 573)

        # Настройка дизайна
        enter_designer_window(self)

        # Настрйка кнопок
        self.ei.pushButton.clicked.connect(self.enter_user_or_not)

    # Проверка пользователя на вход
    def enter_user_or_not(self):
        try:
            id = str(self.ei.lineEdit.text())
            password = str(self.ei.lineEdit_2.text())

            path_programm = os.getcwd()
            path = path_programm + "\\database\\"

            conn = sqlite3.connect(
                path + "mydatabase.db")
            cursor = conn.cursor()

            #sql = "SELECT * FROM Users WHERE id = ? and password= ?"
            cursor.execute("SELECT * FROM Users WHERE id = :id and password = :pass", {"id": id, "pass" : password})

            if cursor.fetchall() == []:
                pass
            else:
                application.show()
                enter_user.close()




        except:
            Error_project.error_18()

#Класс для администрирования
class AdminWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.di = Ui_MainWindow6()
        self.di.setupUi(self)
        self.di.textEdit.setFont(QtGui.QFont('SansSerif', 14))

        # Реализуем combobox
        self.di.comboBox.addItem("User")
        self.di.comboBox.addItem("Admin")
        self.di.comboBox.addItem("Root")

        # Реализуем нажатие кнопок
        self.di.pushButton_2.clicked.connect(self.add_user_file)
        self.di.pushButton.clicked.connect(self.see_all_user)
        self.di.pushButton_3.clicked.connect(self.delete_users_id)

        # Реализуем интерфес
        add_admin_designer(self)

    # Добавляем пользователя
    def add_user_file(self):
        if (self.di.lineEdit.text() != "" and self.di.lineEdit_5.text() != "" and self.di.lineEdit_2.text() != "" \
                and self.di.lineEdit_3.text() != "" and self.di.lineEdit_4.text() != ""):
            add_user_admin(self)


        else:
            Error_project.error_11()

    # Проссматриваем всех пользователей
    def see_all_user(self):
        see_all_users(self)

    # Удаляем пользоавтеля
    def delete_users_id(self):
        delete_user(self)


# Класс для выбора пользователей для обучения нейронной сети
class UserChangeClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ki = Ui_MainWindow8()
        self.ki.setupUi(self)

        # Новые переменные для нейронной сети
        self.id_mass = set()
        self.id_now = None

        # Создание дизайна
        designer_user_change(self)
        self.ki.label.setText("")

        # Настрйока нажатия всех кнопок
        self.ki.pushButton_3.clicked.connect(self.seek_user_method)
        self.ki.pushButton_4.clicked.connect(self.change_all_user)
        self.ki.pushButton_2.clicked.connect(self.add_mass_user)
        self.ki.pushButton_5.clicked.connect(self.step_last)
        # Настройка вывода всех id
        user_change_func(self, helpwindow)

        #Настрйока lineedit
        self.ki.lineEdit.setText("1")
        # Настройка очистка списка

    # Ищем пользователей по id
    def seek_user_method(self):
        seek_user(self, helpwindow)

    # Делаем шаг вперёд по id
    def change_all_user(self):
        try:
            step_seek_user(self, helpwindow)

        except:
            Error_project.error_20()

    #Делаем шаг назад по id
    def step_last(self):
        try:
            step_last_end(self, helpwindow)
        except:
            Error_project.error_20()


    # Заполнение массива индексов
    def add_mass_user(self):
        try:
            self.ki.textEdit_2.clear()
            self.id_mass.add(int(self.id_now))
            for i in self.id_mass:
                self.ki.textEdit_2.append(str(i) + ";")
            print(self.id_mass)
        except:
            Error_project.error_21()


# Класс настройки кмеры
class CameraParams(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pi = Ui_MainWindow9()
        self.pi.setupUi(self)

        # Настройка дизайна
        camera_designer_new(self)

        # Настрйока кнопок
        self.pi.pushButton.clicked.connect(self.camear_save)

        # Настройка параметров камеры
        self.camera_mass = []

    def camear_save(self):
        # Проверяем камеры
        first = self.pi.checkBox.isChecked()
        second = self.pi.checkBox_2.isChecked()
        third = self.pi.checkBox_3.isChecked()
        fourth = self.pi.checkBox_4.isChecked()

        # Добавляем камеры в массив
        if first: self.camera_mass.append(0)
        if second: self.camera_mass.append(1)
        if third: self.camera_mass.append(2)
        if fourth: self.camera_mass.append(3)

        try:
            if not first: self.camera_mass.remove(0)
        except:
            pass
        try:
            if not second: self.camera_mass.remove(1)
        except:
            pass
        try:
            if not third: self.camera_mass.remove(2)
        except:
            pass
        try:
            if not fourth: self.camera_mass.remove(3)
        except:
            pass
        Error_project.error_22()

# Класс для выбора нейронной сети
class NeironChanger(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.nni = Ui_MainWindow11()
        self.nni.setupUi(self)

        self.mass_neiron = []


        #Создаём дизайн
        neiron_change_designer(self)

        #Выводим все нейронные сети
        self.see_all_neirons()

        #Обрабатываем кнопки
        self.nni.pushButton.clicked.connect(self.fixed_change)

        #Закрепляем за каждой камерой нейронную сеть
        self.first_cam = "trainer.yml"
        self.second_cam = "trainer.yml"
        self.third_cam = "trainer.yml"
        self.thourth_cam = "trainer.yml"


    def see_all_neirons(self):
        path_neiron_save = helpwindow.neiron_save

        imagePaths =  os.listdir(path_neiron_save)
        n = 1
        self.mass_neiron.clear()
        for imagePath in imagePaths:
            self.nni.textEdit_2.append(str(n) + ")" + " " + str(imagePath))
            self.mass_neiron.append(imagePath)
            n += 1

    #Метод для закрепления результата камера нейронная сеть
    def fixed_change(self):

        #first
        try:
            first = int(self.nni.textEdit.toPlainText())
            if (first - 1) < len(self.mass_neiron):
                self.first_cam = self.mass_neiron[first - 1]
        except:
            pass

        # second
        try:
            first = int(self.nni.textEdit_3.toPlainText())
            if (first - 1) < len(self.mass_neiron):
                self.second_cam = self.mass_neiron[first - 1]
        except:
            pass

        #third
        try:
            first = int(self.nni.textEdit_4.toPlainText())
            if (first - 1) < len(self.mass_neiron):
                self.third_cam = self.mass_neiron[first - 1]
        except:
            pass

        #thourth
        try:
            first = int(self.nni.textEdit_5.toPlainText())
            if (first - 1) < len(self.mass_neiron):
                self.thourth_cam = self.mass_neiron[first - 1]
        except:
            pass

        Error_project.error_29()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    admins = AdminWindow()
    enter_user = EnterWindow()
    application = mywindow()
    autom_add = Autom_add_user()    # автодобавление пользователя
    thirdapp = ThirdWindows()
    helpwindow = HelpWindows()
    userchange = UserChangeClass()  #выбрать людей
    cameraparam = CameraParams() # отметить используемые камеры
    neirons = NeironChanger() # выбрать файл нейросетей для камер

    enter_user.show()

    sys.exit(app.exec())
