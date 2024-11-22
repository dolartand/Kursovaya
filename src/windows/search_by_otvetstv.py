from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit, QPushButton, QTableView)

class Ui_wndw_search_by_otvetstv(object):
    def setupUi(self, wndw_search_by_otvetstv):
        """
        Метод, который настраивает UI для окна поиска по фамилии ответственного.
        """
        # Установка имени окна, если оно еще не задано
        if not wndw_search_by_otvetstv.objectName():
            wndw_search_by_otvetstv.setObjectName(u"Поиск")

        # Настройка размеров и стиля окна
        wndw_search_by_otvetstv.resize(400, 388)
        wndw_search_by_otvetstv.setStyleSheet(u"background-color: qlineargradient(\n"
                                                "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                                "        stop:0 rgba(139,0,255, 20), \n"
                                                "        stop:1 rgba(115,102,189, 40));")

        # Рамка для поиска
        self.frm_search_by_otvetstv = QFrame(wndw_search_by_otvetstv)
        self.frm_search_by_otvetstv.setObjectName(u"frm_search_by_otvetstv")
        self.frm_search_by_otvetstv.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_otvetstv.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_otvetstv.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_otvetstv.setFrameShadow(QFrame.Shadow.Raised)

        # Заголовок поиска
        self.lbl_search_by_otvetstv = QLabel(self.frm_search_by_otvetstv)
        self.lbl_search_by_otvetstv.setObjectName(u"lbl_search_by_otvetstv")
        self.lbl_search_by_otvetstv.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_otvetstv.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_otvetstv.setFont(font)
        self.lbl_search_by_otvetstv.setStyleSheet(u"background-color: none;\n"
                                                    "border: none;")
        self.lbl_search_by_otvetstv.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Метка для ввода фамилии
        self.lbl_enter_fam = QLabel(self.frm_search_by_otvetstv)
        self.lbl_enter_fam.setObjectName(u"lbl_enter_fam")
        self.lbl_enter_fam.setGeometry(QRect(10, 50, 151, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_fam.setFont(font1)
        self.lbl_enter_fam.setStyleSheet(u"background-color: none;\n"
                                           "border:none;")

        # Поле для ввода фамилии
        self.le_enter_fam = QLineEdit(self.frm_search_by_otvetstv)
        self.le_enter_fam.setObjectName(u"le_enter_fam")
        self.le_enter_fam.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_fam.setFont(font1)

        # Кнопка для вывода результатов
        self.pb_show = QPushButton(self.frm_search_by_otvetstv)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
                                    "color: white;\n"
                                    "background-color: rgba(254,254,34, 30);\n"
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

        # Рамка для таблицы результатов
        self.frm_table_search_by_otvetstv = QFrame(wndw_search_by_otvetstv)
        self.frm_table_search_by_otvetstv.setObjectName(u"frm_table_search_by_otvetstv")
        self.frm_table_search_by_otvetstv.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_otvetstv.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_otvetstv.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_otvetstv.setFrameShadow(QFrame.Shadow.Raised)

        # Таблица для отображения результатов поиска
        self.tv__search_by_otvetstv = QTableView(self.frm_table_search_by_otvetstv)
        self.tv__search_by_otvetstv.setObjectName(u"tv__search_by_otvetstv")
        self.tv__search_by_otvetstv.setGeometry(QRect(10, 10, 361, 221))
        self.tv__search_by_otvetstv.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Вызов метода для задания текста интерфейса
        self.retranslateUi(wndw_search_by_otvetstv)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_search_by_otvetstv)

    def retranslateUi(self, wndw_search_by_otvetstv):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_search_by_otvetstv.setWindowTitle(QCoreApplication.translate("wndw_search_by_otvetstv", u"Поиск", None))
        self.lbl_search_by_otvetstv.setText(QCoreApplication.translate("wndw_search_by_otvetstv", u"Поиск по фамилии ответственного", None))
        self.lbl_enter_fam.setText(QCoreApplication.translate("wndw_search_by_otvetstv", u"Введите фамилию", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_otvetstv", u"Вывести", None))