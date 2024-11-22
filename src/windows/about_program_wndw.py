from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont, QMovie)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QTextEdit)

class Ui_wndw_about_program(object):
    def setupUi(self, wndw_about_program):
        """
        Метод, который настраивает UI для окна "О программе".
        """
        if not wndw_about_program.objectName():
            wndw_about_program.setObjectName(u"О программе")
        wndw_about_program.resize(807, 509)

        # Установка фонового градиента
        wndw_about_program.setStyleSheet(u"background-color: qlineargradient(\n"
                                         "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                         "        stop:0 rgba(139,0,255, 20), \n"
                                         "        stop:1 rgba(115,102,189, 40));")

        # Первый фрейм для GIF
        self.frame = QFrame(wndw_about_program)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 90, 321, 321))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Лейбл для отображения GIF
        self.lbl_gif = QLabel(self.frame)
        self.movie = QMovie(u"assets/database_table.gif")
        self.movie.setScaledSize(QSize(300, 300))
        self.lbl_gif.setMovie(self.movie)
        self.movie.start()
        self.lbl_gif.setObjectName(u"lbl_gif")
        self.lbl_gif.setGeometry(QRect(10, 10, 300, 300))
        self.lbl_gif.setMaximumSize(QSize(640, 640))
        self.lbl_gif.setStyleSheet(u"border: none;\n"
                                   "background-color: none;")

        # Заголовок программы
        self.label_2 = QLabel(wndw_about_program)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 30, 331, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: none;\n"
                                   "border: none;")

        # Второй фрейм для текстового описания
        self.frame_2 = QFrame(wndw_about_program)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(350, 90, 451, 321))
        self.frame_2.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        # Текстовое описание
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 20, 411, 281))
        font1 = QFont()
        font1.setPointSize(16)
        self.textEdit.setFont(font1)
        self.textEdit.setReadOnly(True)

        # Лейбл для версии программы
        self.label = QLabel(wndw_about_program)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 450, 241, 31))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
                                 "background-color: none;")

        # Кнопка "Назад"
        self.pb_back = QPushButton(wndw_about_program)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setGeometry(QRect(550, 440, 191, 51))
        self.pb_back.setFont(font)
        self.pb_back.setStyleSheet(u"QPushButton {\n"
                                   "color: white;\n"
                                   "backgroung-color: rgba(254,254,34, 30);\n"
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

        self.retranslateUi(wndw_about_program)

        QMetaObject.connectSlotsByName(wndw_about_program)
    # setupUi

    def retranslateUi(self, wndw_about_program):
        """
        Устанавливает текстовые значения для виджетов.
        """
        wndw_about_program.setWindowTitle(QCoreApplication.translate("wndw_about_program", "О программе"))
        self.lbl_gif.setText("")
        self.label_2.setText(QCoreApplication.translate("wndw_about_program", "Книга компьютерной техники"))
        self.textEdit.setHtml(QCoreApplication.translate("wndw_about_program",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt;\">\n"
            "<p>Программа позволяет:</p>\n"
            "<ul><li>Получать сведения о состоянии компьютерной техники.</li>\n"
            "<li>Проводить операции с отдельными записями (добавление, удаление, редактирование, поиск).</li>\n"
            "<li>Просматривать удалённые записи в архиве.</li>\n"
            "<li>Сортировать данные по различным критериям.</li></ul>\n"
            "</body></html>"))
        self.label.setText(QCoreApplication.translate("wndw_about_program", "Версия ver. 1.0.0.2024"))
        self.pb_back.setText(QCoreApplication.translate("wndw_about_program", "Назад"))
    # retranslateUi
