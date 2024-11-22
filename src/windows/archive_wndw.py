from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QTableView)


class Ui_wndw_archive(object):
    def setupUi(self, wndw_archive):
        """
        Метод для настройки UI окна "Архив".
        """
        # Установка имени окна, если оно ещё не задано
        if not wndw_archive.objectName():
            wndw_archive.setObjectName("Архив")

        # Настройка размеров и стиля окна
        wndw_archive.resize(801, 467)
        wndw_archive.setStyleSheet(
            "background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "        stop:0 rgba(139,0,255, 20), \n"
            "        stop:1 rgba(115,102,189, 40));"
        )

        # Настройка основной рамки для архива
        self.frame = QFrame(wndw_archive)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 10, 781, 451))
        self.frame.setStyleSheet("background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Заголовок для архива
        self.lbl_archive = QLabel(self.frame)
        self.lbl_archive.setObjectName("lbl_archive")
        self.lbl_archive.setGeometry(QRect(200, 0, 341, 41))
        self.lbl_archive.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_archive.setFont(font)
        self.lbl_archive.setStyleSheet("background-color: none;\nborder: none;")
        self.lbl_archive.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Таблица для отображения архива
        self.tv_archive = QTableView(self.frame)
        self.tv_archive.setObjectName("tv_archive")
        self.tv_archive.setGeometry(QRect(10, 60, 751, 311))
        self.tv_archive.setStyleSheet("background-color: rgba(254,254,34, 10)")

        # Кнопка для удаления записи
        self.pb_delete = QPushButton(self.frame)
        self.pb_delete.setObjectName("pb_delete")
        self.pb_delete.setGeometry(QRect(10, 390, 135, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.pb_delete.setFont(font1)
        self.pb_delete.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(254,254,34, 20);\n"
            "border: 1px solid rgba(254,254,34, 20);\n"
            "border-radius: 7px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(254,254,34, 40);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(254,254,34, 70);\n"
            "}"
        )

        # Кнопка для выхода
        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName("pb_exit")
        self.pb_exit.setGeometry(QRect(160, 390, 131, 41))
        self.pb_exit.setFont(font1)
        self.pb_exit.setStyleSheet(
            "QPushButton {\n"
            "color: white;\n"
            "background-color: rgba(254,254,34, 20);\n"
            "border: 1px solid rgba(254,254,34, 20);\n"
            "border-radius: 7px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: rgba(254,254,34, 40);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(254,254,34, 70);\n"
            "}"
        )

        # Вызов метода для перевода текста интерфейса
        self.retranslateUi(wndw_archive)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_archive)

    def retranslateUi(self, wndw_archive):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_archive.setWindowTitle(QCoreApplication.translate("wndw_archive", "Архив", None))
        self.lbl_archive.setText(QCoreApplication.translate("wndw_archive", "Архив удалённых записей", None))
        self.pb_delete.setText(QCoreApplication.translate("wndw_archive", "Удалить запись", None))
        self.pb_exit.setText(QCoreApplication.translate("wndw_archive", "Назад", None))