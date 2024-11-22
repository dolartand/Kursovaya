from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QGroupBox, QLabel, QLineEdit, QPushButton, QComboBox)


class Ui_wndw_edit(object):
    def setupUi(self, wndw_edit):
        """
        Метод для настройки UI окна "Редактирование записи".
        """
        # Установка имени окна, если оно ещё не задано
        if not wndw_edit.objectName():
            wndw_edit.setObjectName("Редактирование записи")

        # Настройка размеров и стиля окна
        wndw_edit.resize(400, 464)
        wndw_edit.setStyleSheet(
            "background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "        stop:0 rgba(139,0,255, 20), \n"
            "        stop:1 rgba(115,102,189, 40));"
        )

        # Настройка рамки для редактирования
        self.frm_edit = QFrame(wndw_edit)
        self.frm_edit.setObjectName("frm_edit")
        self.frm_edit.setGeometry(QRect(10, 10, 386, 446))
        self.frm_edit.setStyleSheet("background-color: rgba(254,254,34, 5)")
        self.frm_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_edit.setFrameShadow(QFrame.Shadow.Raised)

        # Заголовок редактирования
        self.lbl_edit = QLabel(self.frm_edit)
        self.lbl_edit.setObjectName("lbl_edit")
        self.lbl_edit.setGeometry(QRect(20, 10, 341, 41))
        self.lbl_edit.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_edit.setFont(font)
        self.lbl_edit.setStyleSheet("background-color: none;\nborder: none;")
        self.lbl_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Группа для новых данных
        self.gb_new_data = QGroupBox(self.frm_edit)
        self.gb_new_data.setObjectName("gb_new_data")
        self.gb_new_data.setGeometry(QRect(10, 50, 361, 351))
        font1 = QFont()
        font1.setPointSize(11)
        self.gb_new_data.setFont(font1)
        self.gb_new_data.setStyleSheet("background-color: none;\nborder: 1px solid rgba(254,254,34, 20);")

        # Комбобокс для типа техники
        self.cb_type_tech = QComboBox(self.gb_new_data)
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.setObjectName("cb_type_tech")
        self.cb_type_tech.setGeometry(QRect(10, 30, 341, 31))
        self.cb_type_tech.setFont(font)

        # Метки и поля для ввода
        self.lbl_name = QLabel(self.gb_new_data)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_name.setGeometry(QRect(10, 70, 127, 26))
        font2 = QFont()
        font2.setPointSize(12)
        self.lbl_name.setFont(font2)
        self.lbl_name.setStyleSheet("background-color: none;\nborder: none;")

        self.le_name = QLineEdit(self.gb_new_data)
        self.le_name.setObjectName("le_name")
        self.le_name.setGeometry(QRect(140, 70, 208, 26))
        self.le_name.setFont(font2)

        self.lbl_year = QLabel(self.gb_new_data)
        self.lbl_year.setObjectName("lbl_year")
        self.lbl_year.setGeometry(QRect(10, 110, 127, 26))
        self.lbl_year.setFont(font2)
        self.lbl_year.setStyleSheet("background-color: none;\nborder: none;")

        self.le_year = QLineEdit(self.gb_new_data)
        self.le_year.setObjectName("le_year")
        self.le_year.setGeometry(QRect(140, 110, 208, 26))
        self.le_year.setFont(font2)

        self.lbl_value = QLabel(self.gb_new_data)
        self.lbl_value.setObjectName("lbl_value")
        self.lbl_value.setGeometry(QRect(10, 150, 127, 26))
        self.lbl_value.setFont(font2)
        self.lbl_value.setStyleSheet("background-color: none;\nborder: none;")

        self.le_value = QLineEdit(self.gb_new_data)
        self.le_value.setObjectName("le_value")
        self.le_value.setGeometry(QRect(140, 150, 208, 26))
        self.le_value.setFont(font2)

        self.lbl_amount = QLabel(self.gb_new_data)
        self.lbl_amount.setObjectName("lbl_amount")
        self.lbl_amount.setGeometry(QRect(10, 190, 127, 20))
        self.lbl_amount.setMaximumSize(QSize(150, 20))
        self.lbl_amount.setFont(font2)
        self.lbl_amount.setStyleSheet("background-color: none;\nborder: none;")

        self.le_amount = QLineEdit(self.gb_new_data)
        self.le_amount.setObjectName("le_amount")
        self.le_amount.setGeometry(QRect(140, 190, 208, 26))
        self.le_amount.setFont(font2)

        self.cb_add_sost = QComboBox(self.gb_new_data)
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.setObjectName("cb_add_sost")
        self.cb_add_sost.setGeometry(QRect(160, 230, 187, 31))
        self.cb_add_sost.setFont(font)

        self.lbl_number_aud = QLabel(self.gb_new_data)
        self.lbl_number_aud.setObjectName("lbl_number_aud")
        self.lbl_number_aud.setGeometry(QRect(10, 270, 148, 20))
        self.lbl_number_aud.setMaximumSize(QSize(150, 20))
        self.lbl_number_aud.setFont(font2)
        self.lbl_number_aud.setStyleSheet("background-color: none;\nborder: none;")

        self.le_number_aud = QLineEdit(self.gb_new_data)
        self.le_number_aud.setObjectName("le_number_aud")
        self.le_number_aud.setGeometry(QRect(160, 270, 187, 26))
        self.le_number_aud.setFont(font2)

        self.lbl_otv = QLabel(self.gb_new_data)
        self.lbl_otv.setObjectName("lbl_otv")
        self.lbl_otv.setGeometry(QRect(10, 310, 148, 20))
        self.lbl_otv.setMaximumSize(QSize(150, 20))
        self.lbl_otv.setFont(font2)
        self.lbl_otv.setStyleSheet("background-color: none;\nborder: none;")

        self.le_otvetstv = QLineEdit(self.gb_new_data)
        self.le_otvetstv.setObjectName("le_otvetstv")
        self.le_otvetstv.setGeometry(QRect(160, 310, 187, 26))
        self.le_otvetstv.setFont(font2)

        self.lbl_sost = QLabel(self.gb_new_data)
        self.lbl_sost.setObjectName("lbl_sost")
        self.lbl_sost.setGeometry(QRect(10, 230, 148, 31))
        self.lbl_sost.setFont(font2)
        self.lbl_sost.setStyleSheet("background-color: none;\nborder: none;")

        # Кнопка для сохранения изменений
        self.pb_save = QPushButton(self.frm_edit)
        self.pb_save.setObjectName("pb_save")
        self.pb_save.setGeometry(QRect(20, 410, 341, 28))
        self.pb_save.setFont(font)
        self.pb_save.setStyleSheet(
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
        self.pb_save.setFlat(False)

        # Вызов метода для перевода текста интерфейса
        self.retranslateUi(wndw_edit)

        # Настройка кнопки по умолчанию
        self.pb_save.setDefault(False)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_edit)

    def retranslateUi(self, wndw_edit):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_edit.setWindowTitle(QCoreApplication.translate("wndw_edit", "Редактирование записи", None))
        self.lbl_edit.setText(QCoreApplication.translate("wndw_edit", "Редактирование записи", None))
        self.gb_new_data.setTitle(QCoreApplication.translate("wndw_edit", "Новые данные", None))
        self.cb_type_tech.setItemText(0, QCoreApplication.translate("wndw_edit", "Процессор", None))
        self.cb_type_tech.setItemText(1, QCoreApplication.translate("wndw_edit", "Материнская плата", None))
        self.cb_type_tech.setItemText(2, QCoreApplication.translate("wndw_edit", "Видеокарта", None))
        self.cb_type_tech.setItemText(3, QCoreApplication.translate("wndw_edit", "Оперативная память", None))
        self.cb_type_tech.setItemText(4, QCoreApplication.translate("wndw_edit", "SSD", None))
        self.cb_type_tech.setItemText(5, QCoreApplication.translate("wndw_edit", "Жёсткий диск", None))
        self.cb_type_tech.setItemText(6, QCoreApplication.translate("wndw_edit", "Блок питания", None))
        self.cb_type_tech.setItemText(7, QCoreApplication.translate("wndw_edit", "Корпус", None))

        self.lbl_name.setText(QCoreApplication.translate("wndw_edit", "Название", None))
        self.lbl_year.setText(QCoreApplication.translate("wndw_edit", "Год выпуска", None))
        self.lbl_value.setText(QCoreApplication.translate("wndw_edit", "Стоимость", None))
        self.lbl_amount.setText(QCoreApplication.translate("wndw_edit", "Кол-во на складе", None))
        self.cb_add_sost.setItemText(0, QCoreApplication.translate("wndw_edit", "В работе", None))
        self.cb_add_sost.setItemText(1, QCoreApplication.translate("wndw_edit", "В ремонте", None))
        self.cb_add_sost.setItemText(2, QCoreApplication.translate("wndw_edit", "Списана", None))

        self.lbl_number_aud.setText(QCoreApplication.translate("wndw_edit", "Номер аудитории", None))
        self.lbl_otv.setText(QCoreApplication.translate("wndw_edit", "Фамилия ответственного", None))
        self.lbl_sost.setText(QCoreApplication.translate("wndw_edit", "Состояние техники", None))
        self.pb_save.setText(QCoreApplication.translate("wndw_edit", "Сохранить изменения", None))