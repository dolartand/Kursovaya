from PySide6.QtCore import (QCoreApplication, QRect, QMetaObject)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton

class Ui_wndw_splash_screen(object):
    def setupUi(self, wndw_splash_screen):
        """
        Метод для настройки пользовательского интерфейса окна заставки.
        """
        if not wndw_splash_screen.objectName():
            wndw_splash_screen.setObjectName(u"SplashScreen")

        # Установка размера окна и фона
        wndw_splash_screen.resize(807, 520)
        wndw_splash_screen.setStyleSheet(u"background-color: white;")

        # Создание и настройка меток
        self.label = QLabel(wndw_splash_screen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 381, 21))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black;")

        # Текстовые метки
        self.label_2 = QLabel(wndw_splash_screen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 40, 421, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: black;")

        self.label_3 = QLabel(wndw_splash_screen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 70, 461, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: black;")

        self.label_4 = QLabel(wndw_splash_screen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 150, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: black;")

        self.label_5 = QLabel(wndw_splash_screen)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 190, 311, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: black;")

        self.label_6 = QLabel(wndw_splash_screen)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 220, 341, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: black;")

        self.label_7 = QLabel(wndw_splash_screen)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 270, 261, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: black;")

        self.label_8 = QLabel(wndw_splash_screen)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(520, 300, 191, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: black;")

        self.label_9 = QLabel(wndw_splash_screen)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 350, 211, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: black;")

        self.label_10 = QLabel(wndw_splash_screen)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(520, 380, 231, 21))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: black;")

        self.label_11 = QLabel(wndw_splash_screen)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(360, 410, 91, 21))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: black;")

        # Логотип на экране заставки
        self.label_12 = QLabel(wndw_splash_screen)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 250, 131, 151))
        self.label_12.setPixmap(QPixmap(u"resourses/splash_screen_logo.png"))

        # Кнопка для перехода дальше
        self.pb_next = QPushButton(wndw_splash_screen)
        self.pb_next.setObjectName(u"pb_next")
        self.pb_next.setGeometry(QRect(20, 440, 391, 51))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        self.pb_next.setFont(font2)
        self.pb_next.setStyleSheet(u"color: black;")

        # Кнопка выхода
        self.pb_exit = QPushButton(wndw_splash_screen)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(410, 440, 391, 51))
        self.pb_exit.setFont(font2)
        self.pb_exit.setStyleSheet(u"color: black;")

        # Установка текста для элементов интерфейса
        self.retranslateUi(wndw_splash_screen)

        QMetaObject.connectSlotsByName(wndw_splash_screen)
    # setupUi

    def retranslateUi(self, wndw_splash_screen):
        """
        Метод для установки текста для элементов интерфейса.
        """
        wndw_splash_screen.setWindowTitle(QCoreApplication.translate("wndw_splash_screen", u"SplashScreen", None))
        self.label.setText(QCoreApplication.translate("wndw_splash_screen", u"Белорусский национальный технический университет", None))
        self.label_2.setText(QCoreApplication.translate("wndw_splash_screen", u"Факультет информационных технологий и робототехники", None))
        self.label_3.setText(QCoreApplication.translate("wndw_splash_screen", u"Кафедра программного обеспечения информационных технологий", None))
        self.label_4.setText(QCoreApplication.translate("wndw_splash_screen", u"Курсовая работа", None))
        self.label_5.setText(QCoreApplication.translate("wndw_splash_screen", u"по дисциплине \"Языки программирования\"", None))
        self.label_6.setText(QCoreApplication.translate("wndw_splash_screen", u"Книга компьютерной техники", None))
        self.label_7.setText(QCoreApplication.translate("wndw_splash_screen", u"Выполнил: студент группы 10701323", None))
        self.label_8.setText(QCoreApplication.translate("wndw_splash_screen", u"Доленко Артур Андреевич", None))
        self.label_9.setText(QCoreApplication.translate("wndw_splash_screen", u"Преподаватель: к.ф.-м.н., доц.", None))
        self.label_10.setText(QCoreApplication.translate("wndw_splash_screen", u"Сидорик Валерий Владимирович", None))
        self.label_11.setText(QCoreApplication.translate("wndw_splash_screen", u"Минск, 2024", None))
        self.label_12.setText("")  # Логотип
        self.pb_next.setText(QCoreApplication.translate("wndw_splash_screen", u"Далее", None))
        self.pb_exit.setText(QCoreApplication.translate("wndw_splash_screen", u"Выход", None))
    # retranslateUi