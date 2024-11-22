from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton)


class Ui_wndw_delete(object):
    def setupUi(self, wndw_delete):
        """
        Метод для настройки UI окна "Удаление записи".
        """
        # Установка имени окна, если оно ещё не задано
        if not wndw_delete.objectName():
            wndw_delete.setObjectName("Удаление записи")

        # Настройка размеров и стиля окна
        wndw_delete.resize(382, 210)
        wndw_delete.setStyleSheet(
            "background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "        stop:0 rgba(139,0,255, 20), \n"
            "        stop:1 rgba(115,102,189, 40));"
        )

        # Настройка рамки для окна удаления
        self.frm_delete = QFrame(wndw_delete)
        self.frm_delete.setObjectName("frm_delete")
        self.frm_delete.setGeometry(QRect(20, 10, 341, 181))
        self.frm_delete.setStyleSheet("background-color: rgba(254,254,34, 5)")
        self.frm_delete.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_delete.setFrameShadow(QFrame.Shadow.Raised)

        # Заголовок окна
        self.lbl_delete = QLabel(self.frm_delete)
        self.lbl_delete.setObjectName("lbl_delete")
        self.lbl_delete.setGeometry(QRect(0, 10, 341, 30))
        self.lbl_delete.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(20)
        self.lbl_delete.setFont(font)
        self.lbl_delete.setStyleSheet("background-color: none;\nborder: none;")
        self.lbl_delete.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Вопрос о подтверждении удаления
        self.lbl_really_delete = QLabel(self.frm_delete)
        self.lbl_really_delete.setObjectName("lbl_really_delete")
        self.lbl_really_delete.setGeometry(QRect(10, 70, 321, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_really_delete.setFont(font1)
        self.lbl_really_delete.setStyleSheet("background-color: none;\nborder: none;")

        # Кнопка "Да" для подтверждения удаления
        self.pb_yes = QPushButton(self.frm_delete)
        self.pb_yes.setObjectName("pb_yes")
        self.pb_yes.setGeometry(QRect(70, 120, 91, 34))
        font2 = QFont()
        font2.setPointSize(14)
        self.pb_yes.setFont(font2)
        self.pb_yes.setStyleSheet(
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

        # Кнопка "Нет" для отмены удаления
        self.pb_no = QPushButton(self.frm_delete)
        self.pb_no.setObjectName("pb_no")
        self.pb_no.setGeometry(QRect(180, 120, 81, 34))
        self.pb_no.setFont(font2)
        self.pb_no.setStyleSheet(
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
        self.retranslateUi(wndw_delete)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_delete)

    def retranslateUi(self, wndw_delete):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_delete.setWindowTitle(QCoreApplication.translate("wndw_delete", "Удаление записи", None))
        self.lbl_delete.setText(QCoreApplication.translate("wndw_delete", "Удаление записи", None))
        self.lbl_really_delete.setText(
            QCoreApplication.translate("wndw_delete", "Вы действительно хотите удалить запись?", None))
        self.pb_yes.setText(QCoreApplication.translate("wndw_delete", "Да", None))
        self.pb_no.setText(QCoreApplication.translate("wndw_delete", "Нет", None))