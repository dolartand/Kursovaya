from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QTableView

class Ui_wndw_search_by_year(object):
    def setupUi(self, wndw_search_by_year):
        """
        Метод для настройки UI окна поиска по году выпуска техники.
        """
        if not wndw_search_by_year.objectName():
            wndw_search_by_year.setObjectName(u"Поиск")

        # Устанавливаем размер окна и стиль
        wndw_search_by_year.resize(400, 390)
        wndw_search_by_year.setStyleSheet(u"background-color: qlineargradient(\n"
                                            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                            "        stop:0 rgba(139,0,255, 20), \n"
                                            "        stop:1 rgba(115,102,189, 40));")

        # Фрейм для отображения результатов поиска
        self.frm_table_search_by_year = QFrame(wndw_search_by_year)
        self.frm_table_search_by_year.setObjectName(u"frm_table_search_by_year")
        self.frm_table_search_by_year.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_year.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_year.setFrameShadow(QFrame.Shadow.Raised)

        # Таблица для отображения результатов поиска
        self.tv_search_by_year = QTableView(self.frm_table_search_by_year)
        self.tv_search_by_year.setObjectName(u"tv_search_by_year")
        self.tv_search_by_year.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Фрейм для ввода данных поиска
        self.frm_search_by_year = QFrame(wndw_search_by_year)
        self.frm_search_by_year.setObjectName(u"frm_search_by_year")
        self.frm_search_by_year.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_year.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_year.setFrameShadow(QFrame.Shadow.Raised)

        # Метка для заголовка поиска
        self.lbl_search_by_year = QLabel(self.frm_search_by_year)
        self.lbl_search_by_year.setObjectName(u"lbl_search_by_year")
        self.lbl_search_by_year.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_year.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_year.setFont(font)
        self.lbl_search_by_year.setStyleSheet(u"background-color: none;\n"
                                               "border: none;")
        self.lbl_search_by_year.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Метка для ввода года
        self.lbl_enter_year = QLabel(self.frm_search_by_year)
        self.lbl_enter_year.setObjectName(u"lbl_enter_year")
        self.lbl_enter_year.setGeometry(QRect(10, 50, 151, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_year.setFont(font1)
        self.lbl_enter_year.setStyleSheet(u"background-color: none;\n"
                                            "border:none;")

        # Поле ввода для года
        self.le_enter_year = QLineEdit(self.frm_search_by_year)
        self.le_enter_year.setObjectName(u"le_enter_year")
        self.le_enter_year.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_year.setFont(font1)

        # Кнопка для отображения результатов
        self.pushButton = QPushButton(self.frm_search_by_year)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 90, 151, 24))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                       "color: white;\n"
                                       "background-color: rgba(254,254,34, 30);\n"  # Исправлено название цвета
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

        # Вызов метода для установки текста для элементов интерфейса
        self.retranslateUi(wndw_search_by_year)

        # Подключение сигналов и слотов
        QMetaObject.connectSlotsByName(wndw_search_by_year)

    def retranslateUi(self, wndw_search_by_year):
        """
        Метод для установки текста для элементов интерфейса.
        """
        wndw_search_by_year.setWindowTitle(QCoreApplication.translate("wndw_search_by_year", u"Поиск", None))
        self.lbl_search_by_year.setText(QCoreApplication.translate("wndw_search_by_year", u"Поиск по году выпуска техники", None))
        self.lbl_enter_year.setText(QCoreApplication.translate("wndw_search_by_year", u"Введите год выпуска", None))
        self.pushButton.setText(QCoreApplication.translate("wndw_search_by_year", u"Вывести", None))