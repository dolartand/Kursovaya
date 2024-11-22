# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_by_number_aud.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QRect, Qt, QSize, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QTableView


class Ui_wndw_search_by_numbe_aud(object):
    def setupUi(self, wndw_search_by_numbe_aud):
        """
        Метод для настройки пользовательского интерфейса окна поиска по номеру аудитории.
        """
        if not wndw_search_by_numbe_aud.objectName():
            wndw_search_by_numbe_aud.setObjectName(u"Поиск")

        # Установка размера и стиля фона окна
        wndw_search_by_numbe_aud.resize(400, 393)
        wndw_search_by_numbe_aud.setStyleSheet(u"background-color: qlineargradient(\n"
                                               "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                               "        stop:0 rgba(139,0,255, 20), \n"
                                               "        stop:1 rgba(115,102,189, 40));")

        # Фрейм для ввода номера аудитории
        self.frm_search_by_number_aud = QFrame(wndw_search_by_numbe_aud)
        self.frm_search_by_number_aud.setObjectName(u"frm_search_by_number_aud")
        self.frm_search_by_number_aud.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_number_aud.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_number_aud.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_number_aud.setFrameShadow(QFrame.Shadow.Raised)

        # Заголовок поиска
        self.lbl_search_by_number = QLabel(self.frm_search_by_number_aud)
        self.lbl_search_by_number.setObjectName(u"lbl_search_by_number")
        self.lbl_search_by_number.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_number.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_number.setFont(font)
        self.lbl_search_by_number.setStyleSheet(u"background-color: none;\n"
                                                "border: none;")
        self.lbl_search_by_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Метка для ввода номера аудитории
        self.lbl_enter_number = QLabel(self.frm_search_by_number_aud)
        self.lbl_enter_number.setObjectName(u"lbl_enter_number")
        self.lbl_enter_number.setGeometry(QRect(10, 50, 151, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_number.setFont(font1)
        self.lbl_enter_number.setStyleSheet(u"background-color: none;\n"
                                            "border:none;")

        # Поле ввода для номера аудитории
        self.le_enter_number = QLineEdit(self.frm_search_by_number_aud)
        self.le_enter_number.setObjectName(u"le_enter_number")
        self.le_enter_number.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_number.setFont(font1)

        # Кнопка для отображения результатов
        self.pb_show = QPushButton(self.frm_search_by_number_aud)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
                                   "color: white;\n"
                                   "background-color: rgba(254,254,34, 20);\n"  # Исправлено название цвета
                                   "border: 1px solid rgba(254,254,34, 20);\n"
                                   "border-radius: 7px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgba(254,254,34, 40);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "background-color: rgba(254,254,34, 70);\n"
                                   "}")

        # Фрейм для отображения результатов поиска
        self.frm_table_search_by_number_aud = QFrame(wndw_search_by_numbe_aud)
        self.frm_table_search_by_number_aud.setObjectName(u"frm_table_search_by_number_aud")
        self.frm_table_search_by_number_aud.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_number_aud.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_number_aud.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_number_aud.setFrameShadow(QFrame.Shadow.Raised)

        # Таблица для отображения результатов поиска
        self.tv__search_by_number = QTableView(self.frm_table_search_by_number_aud)
        self.tv__search_by_number.setObjectName(u"tv__search_by_number")
        self.tv__search_by_number.setGeometry(QRect(10, 10, 361, 221))
        self.tv__search_by_number.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Установка текста для элементов интерфейса
        self.retranslateUi(wndw_search_by_numbe_aud)

        QMetaObject.connectSlotsByName(wndw_search_by_numbe_aud)

    def retranslateUi(self, wndw_search_by_numbe_aud):
        """
        Метод для установки текста для элементов интерфейса.
        """
        wndw_search_by_numbe_aud.setWindowTitle(QCoreApplication.translate("wndw_search_by_numbe_aud", u"Поиск", None))
        self.lbl_search_by_number.setText(
            QCoreApplication.translate("wndw_search_by_numbe_aud", u"Поиск по номеру аудитории", None))
        self.lbl_enter_number.setText(
            QCoreApplication.translate("wndw_search_by_numbe_aud", u"Введите номер ауд.", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_numbe_aud", u"Вывести", None))