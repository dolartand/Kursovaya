from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QComboBox, QTableView)

class Ui_search_by_condition_wndw(object):
    def setupUi(self, search_by_condition_wndw):
        """
        Метод, который настраивает UI для окна поиска по состоянию техники.
        """
        # Установка имени окна, если оно еще не задано
        if not search_by_condition_wndw.objectName():
            search_by_condition_wndw.setObjectName(u"Поиск")

        # Настройка размеров и стиля окна
        search_by_condition_wndw.resize(400, 394)
        search_by_condition_wndw.setStyleSheet(u"background-color: qlineargradient(\n"
                                                "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                                "        stop:0 rgba(139,0,255, 20), \n"
                                                "        stop:1 rgba(115,102,189, 40));")

        # Добавление и настройка рамки для поиска
        self.frm_search_by_condition = QFrame(search_by_condition_wndw)
        self.frm_search_by_condition.setObjectName(u"frm_search_by_condition")
        self.frm_search_by_condition.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_condition.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_condition.setFrameShadow(QFrame.Shadow.Raised)

        # Метка для заголовка поиска
        self.lbl_search_by_condition = QLabel(self.frm_search_by_condition)
        self.lbl_search_by_condition.setObjectName(u"lbl_search_by_condition")
        self.lbl_search_by_condition.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_condition.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_condition.setFont(font)
        self.lbl_search_by_condition.setStyleSheet(u"background-color: none;\n"
                                                   "border: none;")
        self.lbl_search_by_condition.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Метка для выбора состояния
        self.lbl_enter_condition = QLabel(self.frm_search_by_condition)
        self.lbl_enter_condition.setObjectName(u"lbl_enter_condition")
        self.lbl_enter_condition.setGeometry(QRect(10, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_condition.setFont(font1)
        self.lbl_enter_condition.setStyleSheet(u"background-color: none;\n"
                                               "border:none;")

        # Кнопка для вывода результатов
        self.pb_show = QPushButton(self.frm_search_by_condition)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
                                    "color: white;\n"
                                    "background-color: rgba(254,254,34, 20);\n"
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

        # Комбобокс для выбора состояния
        self.cb_condition = QComboBox(self.frm_search_by_condition)
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.setObjectName(u"cb_condition")
        self.cb_condition.setGeometry(QRect(180, 40, 191, 31))
        self.cb_condition.setFont(font)

        # Рамка для таблицы результатов
        self.frm_table_search_by_condition = QFrame(search_by_condition_wndw)
        self.frm_table_search_by_condition.setObjectName(u"frm_table_search_by_condition")
        self.frm_table_search_by_condition.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_condition.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_condition.setFrameShadow(QFrame.Shadow.Raised)

        # Таблица для отображения результатов поиска
        self.tv_search_by_condition = QTableView(self.frm_table_search_by_condition)
        self.tv_search_by_condition.setObjectName(u"tv_search_by_condition")
        self.tv_search_by_condition.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Вызов метода для задания текста интерфейса
        self.retranslateUi(search_by_condition_wndw)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(search_by_condition_wndw)

    def retranslateUi(self, search_by_condition_wndw):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        search_by_condition_wndw.setWindowTitle(QCoreApplication.translate("search_by_condition_wndw", u"Поиск", None))
        self.lbl_search_by_condition.setText(QCoreApplication.translate("search_by_condition_wndw", u"Поиск по состоянию техники", None))
        self.lbl_enter_condition.setText(QCoreApplication.translate("search_by_condition_wndw", u"Выберите состояние", None))
        self.pb_show.setText(QCoreApplication.translate("search_by_condition_wndw", u"Вывести", None))
        self.cb_condition.setItemText(0, QCoreApplication.translate("search_by_condition_wndw", u"В работе", None))
        self.cb_condition.setItemText(1, QCoreApplication.translate("search_by_condition_wndw", u"В ремонте", None))
        self.cb_condition.setItemText(2, QCoreApplication.translate("search_by_condition_wndw", u"Списана", None))