from PySide6.QtCore import (QCoreApplication, QRect, QSize, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel, QLineEdit,
                               QPushButton, QComboBox)


class Ui_wndw_add(object):
    def setupUi(self, wndw_add):
        """
        Метод, который настраивает UI для окна "Добавление записи".
        """
        # Установка имени окна, если оно еще не задано
        if not wndw_add.objectName():
            wndw_add.setObjectName("Добавление записи")

        # Настройка размеров и стиля окна
        wndw_add.resize(400, 543)
        wndw_add.setStyleSheet(
            "background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "        stop:0 rgba(139,0,255, 20), \n"
            "        stop:1 rgba(115,102,189, 40));"
        )

        # Настройка рамки для добавления записи
        self.frm_add = QFrame(wndw_add)
        self.frm_add.setObjectName("frm_add")
        self.frm_add.setGeometry(QRect(20, 10, 361, 521))
        self.frm_add.setStyleSheet("background-color: rgba(254,254,34, 5)")
        self.frm_add.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_add.setFrameShadow(QFrame.Shadow.Raised)

        # Создание сетки для расположения элементов
        self.gridLayout = QGridLayout(self.frm_add)
        self.gridLayout.setObjectName("gridLayout")

        # Поле ввода значения
        self.le_value = QLineEdit(self.frm_add)
        self.le_value.setObjectName("le_value")
        font = QFont()
        font.setPointSize(12)
        self.le_value.setFont(font)
        self.gridLayout.addWidget(self.le_value, 4, 1, 1, 1)

        # Метка для номера аудитории
        self.lbl_number_aud = QLabel(self.frm_add)
        self.lbl_number_aud.setObjectName("lbl_number_aud")
        self.lbl_number_aud.setMaximumSize(QSize(150, 20))
        self.lbl_number_aud.setFont(font)
        self.lbl_number_aud.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_number_aud, 7, 0, 1, 1)

        # Метка для названия
        self.lbl_name = QLabel(self.frm_add)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_name, 2, 0, 1, 1)

        # Поле ввода года
        self.le_year = QLineEdit(self.frm_add)
        self.le_year.setObjectName("le_year")
        self.le_year.setFont(font)
        self.gridLayout.addWidget(self.le_year, 3, 1, 1, 1)

        # Метка для года
        self.lbl_year = QLabel(self.frm_add)
        self.lbl_year.setObjectName("lbl_year")
        self.lbl_year.setFont(font)
        self.lbl_year.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_year, 3, 0, 1, 1)

        # Метка для состояния техники
        self.lbl_sost = QLabel(self.frm_add)
        self.lbl_sost.setObjectName("lbl_sost")
        self.lbl_sost.setFont(font)
        self.lbl_sost.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_sost, 6, 0, 1, 1)

        # Метка для фамилии ответственного
        self.lbl_otv = QLabel(self.frm_add)
        self.lbl_otv.setObjectName("lbl_otv")
        self.lbl_otv.setMaximumSize(QSize(150, 20))
        self.lbl_otv.setFont(font)
        self.lbl_otv.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_otv, 8, 0, 1, 1)

        # Поле ввода названия
        self.le_name = QLineEdit(self.frm_add)
        self.le_name.setObjectName("le_name")
        self.le_name.setFont(font)
        self.gridLayout.addWidget(self.le_name, 2, 1, 1, 1)

        # Кнопка для добавления записи
        self.pb_add = QPushButton(self.frm_add)
        self.pb_add.setObjectName("pb_add")
        font1 = QFont()
        font1.setPointSize(14)
        self.pb_add.setFont(font1)
        self.pb_add.setStyleSheet(
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
        self.pb_add.setFlat(False)
        self.gridLayout.addWidget(self.pb_add, 9, 0, 1, 2)

        # Метка для стоимости
        self.lbl_value = QLabel(self.frm_add)
        self.lbl_value.setObjectName("lbl_value")
        self.lbl_value.setFont(font)
        self.lbl_value.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_value, 4, 0, 1, 1)

        # Поле ввода количества
        self.le_amount = QLineEdit(self.frm_add)
        self.le_amount.setObjectName("le_amount")
        self.le_amount.setFont(font)
        self.gridLayout.addWidget(self.le_amount, 5, 1, 1, 1)

        # Комбобокс для состояния техники
        self.cb_add_sost = QComboBox(self.frm_add)
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.setObjectName("cb_add_sost")
        self.cb_add_sost.setFont(font1)
        self.gridLayout.addWidget(self.cb_add_sost, 6, 1, 1, 1)

        # Поле ввода номера аудитории
        self.le_number_aud = QLineEdit(self.frm_add)
        self.le_number_aud.setObjectName("le_number_aud")
        self.le_number_aud.setFont(font)
        self.gridLayout.addWidget(self.le_number_aud, 7, 1, 1, 1)

        # Метка для количества
        self.lbl_amount = QLabel(self.frm_add)
        self.lbl_amount.setObjectName("lbl_amount")
        self.lbl_amount.setMaximumSize(QSize(150, 20))
        self.lbl_amount.setFont(font)
        self.lbl_amount.setStyleSheet("background-color: none;\nborder: none;")
        self.gridLayout.addWidget(self.lbl_amount, 5, 0, 1, 1)

        # Заголовок для добавления записи
        self.lbl_add = QLabel(self.frm_add)
        self.lbl_add.setObjectName("lbl_add")
        self.lbl_add.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(20)
        self.lbl_add.setFont(font2)
        self.lbl_add.setStyleSheet("background-color: none;\nborder: none;")
        self.lbl_add.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.lbl_add, 0, 0, 1, 2)

        # Комбобокс для типа
        self.cb_add_type = QComboBox(self.frm_add)
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.setObjectName("cb_add_type")
        self.cb_add_type.setFont(font1)
        self.gridLayout.addWidget(self.cb_add_type, 1, 0, 1, 2)

        # Поле ввода фамилии ответственного
        self.le_otvetstv = QLineEdit(self.frm_add)
        self.le_otvetstv.setObjectName("le_otvetstv")
        self.le_otvetstv.setFont(font)
        self.gridLayout.addWidget(self.le_otvetstv, 8, 1, 1, 1)

        # Вызов метода для задания текста интерфейса
        self.retranslateUi(wndw_add)

        # Настройка кнопки по умолчанию
        self.pb_add.setDefault(False)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_add)

    def retranslateUi(self, wndw_add):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_add.setWindowTitle(QCoreApplication.translate("wndw_add", "Добавление записи"))
        self.lbl_number_aud.setText(QCoreApplication.translate("wndw_add", "Номер аудитории"))
        self.lbl_name.setText(QCoreApplication.translate("wndw_add", "Название"))
        self.lbl_year.setText(QCoreApplication.translate("wndw_add", "Год выпуска"))
        self.lbl_sost.setText(QCoreApplication.translate("wndw_add", "Состояние техники"))
        self.lbl_otv.setText(QCoreApplication.translate("wndw_add", "Фамилия ответственного"))
        self.pb_add.setText(QCoreApplication.translate("wndw_add", "Добавить запись"))
        self.lbl_value.setText(QCoreApplication.translate("wndw_add", "Стоимость"))

        # Настройка элементов комбобокса состояния техники
        self.cb_add_sost.setItemText(0, QCoreApplication.translate("wndw_add", "В работе"))
        self.cb_add_sost.setItemText(1, QCoreApplication.translate("wndw_add", "В ремонте"))
        self.cb_add_sost.setItemText(2, QCoreApplication.translate("wndw_add", "Списана"))

        self.lbl_amount.setText(QCoreApplication.translate("wndw_add", "Кол-во на складе"))
        self.lbl_add.setText(QCoreApplication.translate("wndw_add", "Добавление записи"))

        # Настройка элементов комбобокса типа
        self.cb_add_type.setItemText(0, QCoreApplication.translate("wndw_add", "Процессор"))
        self.cb_add_type.setItemText(1, QCoreApplication.translate("wndw_add", "Материнская плата"))
        self.cb_add_type.setItemText(2, QCoreApplication.translate("wndw_add", "Видеокарта"))
        self.cb_add_type.setItemText(3, QCoreApplication.translate("wndw_add", "Оперативная память"))
        self.cb_add_type.setItemText(4, QCoreApplication.translate("wndw_add", "SSD"))
        self.cb_add_type.setItemText(5, QCoreApplication.translate("wndw_add", "Жёсткий диск"))
        self.cb_add_type.setItemText(6, QCoreApplication.translate("wndw_add", "Блок питания"))
        self.cb_add_type.setItemText(7, QCoreApplication.translate("wndw_add", "Корпус"))