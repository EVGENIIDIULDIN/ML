from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Error_project(object):

    @staticmethod
    def error_1():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Заполните поля (номер) и (фрейм) и (имя)")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_2():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ошибка при вводе значений")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_3():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Через 3 секунды наснётся обработка лица. Смотрите в фронтальную камеру")
        msgBox.setWindowTitle("Предупреждение")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_4():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Программа завершила свою работу")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_5():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Вы некорректно заполнили поля")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_6():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Значения установлены")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_7():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ошибка при настройке камеры")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_8():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ошибка при обучении нейронной сети")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_9():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Директория очищена")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_10():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Непредвиденная ошибка перезапустите программу и проверьте файлы в директориях")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_11():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Заполните все поля")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_12():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Проверьте файл Privileges.txt")
        msgBox.setWindowTitle("Ошибка")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_13():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Пользователь добавлен")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_14():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Данный id уже существует")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_15():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Введите id")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_16():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ошибка при удалении пользователя")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_17():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Пользователь удалён")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_18():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Введены неверные данные")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_19():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Проверьте правильность id(шага)")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_20():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Выберите начальное значение id")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_21():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ошибка при добавлении пользователя")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_22():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Изменения внесены")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_23():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Достигнуто нулевое значение")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_24():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Данный id отсутствует")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_25():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Вы оставили стандартное название")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_26():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Введено более 120 символов")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_27():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Тренировка завершена")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_28():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Проверьте корректность значений")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_29():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Изменения внесены")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_30():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Проверьте настройки нейронной сети и камеры")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()

    @staticmethod
    def error_31():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Очистка произведена")
        msgBox.setWindowTitle("ОК")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect()
        returnValue = msgBox.exec()