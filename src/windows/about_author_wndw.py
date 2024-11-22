from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QPushButton

class Ui_wndw_about_author(object):
    def setupUi(self, wndw_about_author):
        """
        Метод, который настраивает UI для окна "Об авторе".
        """
        # Установка имени окна, если оно еще не задано
        if not wndw_about_author.objectName():
            wndw_about_author.setObjectName("Об авторе")

        # Настройка размеров и стиля окна
        wndw_about_author.resize(400, 528)
        wndw_about_author.setStyleSheet(
            "background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
            "        stop:0 rgba(139,0,255, 20), \n"
            "        stop:1 rgba(115,102,189, 40));"
        )

        # Добавление и настройка рамки (frame)
        self.frame = QFrame(wndw_about_author)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 10, 381, 511))
        self.frame.setStyleSheet("background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Добавление и настройка основного изображения (label)
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 361, 291))
        self.label.setStyleSheet("background-color: none;\nborder: none;")
        self.label.setPixmap(QPixmap("assets/author_image.jpg"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Добавление и настройка текста "Автор" (label_2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(150, 300, 71, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\nborder: none;")

        # Добавление информации о группе студента (label_3)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(60, 340, 251, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet("background-color: none;\nborder: none;")

        # Добавление имени автора (label_4)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(60, 380, 271, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet("background-color: none;\nborder: none;")

        # Добавление электронной почты автора (label_5)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(90, 420, 211, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet("background-color: none;\nborder: none;")

        # Добавление кнопки "Назад" (pb_back)
        self.pb_back = QPushButton(self.frame)
        self.pb_back.setObjectName("pb_back")
        self.pb_back.setGeometry(QRect(20, 460, 341, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.pb_back.setFont(font2)
        self.pb_back.setStyleSheet(
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
        self.pb_back.setFlat(False)

        # Вызов метода для задания текста интерфейса
        self.retranslateUi(wndw_about_author)

        # Настройка кнопки по умолчанию
        self.pb_back.setDefault(False)

        # Соединение слотов и сигналов
        QMetaObject.connectSlotsByName(wndw_about_author)

    def retranslateUi(self, wndw_about_author):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        wndw_about_author.setWindowTitle(QCoreApplication.translate("wndw_about_author", "Об авторе"))
        self.label.setText("")  # Изображение уже задано через Pixmap
        self.label_2.setText(QCoreApplication.translate("wndw_about_author", "Автор"))
        self.label_3.setText(QCoreApplication.translate("wndw_about_author", "Студент группы 10701323"))
        self.label_4.setText(QCoreApplication.translate("wndw_about_author", "Доленко Артур Андреевич"))
        self.label_5.setText(QCoreApplication.translate("wndw_about_author", "dolartand@gmail.com"))
        self.pb_back.setText(QCoreApplication.translate("wndw_about_author", "Назад"))