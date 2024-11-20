# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_program_wndw.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_wndw_about_program(object):
    def setupUi(self, wndw_about_program):
        if not wndw_about_program.objectName():
            wndw_about_program.setObjectName(u"О программе")
        wndw_about_program.resize(807, 509)
        wndw_about_program.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frame = QFrame(wndw_about_program)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 90, 321, 321))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_gif = QLabel(self.frame)
        self.movie = QMovie(u"resourses/database_table.gif")
        self.movie.setScaledSize(QSize(300, 300))
        self.lbl_gif.setMovie(self.movie)
        self.movie.start()
        self.lbl_gif.setObjectName(u"lbl_gif")
        self.lbl_gif.setGeometry(QRect(10, 10, 300, 300))
        self.lbl_gif.setMaximumSize(QSize(640, 640))
        self.lbl_gif.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.label_2 = QLabel(wndw_about_program)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 30, 331, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.frame_2 = QFrame(wndw_about_program)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(350, 90, 451, 321))
        self.frame_2.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 20, 411, 281))
        font1 = QFont()
        font1.setPointSize(16)
        self.textEdit.setFont(font1)
        self.textEdit.setReadOnly(True)
        self.label = QLabel(wndw_about_program)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 450, 241, 31))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
"background-color: none;")
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
        wndw_about_program.setWindowTitle(QCoreApplication.translate("wndw_about_program", u"О программе", None))
        self.lbl_gif.setText("")
        self.label_2.setText(QCoreApplication.translate("wndw_about_program", u"\u041a\u043d\u0438\u0433\u0430 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.textEdit.setHtml(QCoreApplication.translate("wndw_about_program", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1. \u041f\u043e\u043b\u0443\u0447\u0430\u0442\u044c \u0441\u0432\u0435\u0434\u0435\u043d\u0438"
                        "\u044f \u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2. \u041f\u0440\u043e\u0432\u043e\u0434\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0441 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438(\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435, \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0438\u0441\u043a \u043f\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u043c\u0443 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u044e).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">3. \u041f\u0440\u043e\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0442\u044c \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0430\u0440\u0445\u0438\u0432\u0435.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">4. \u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u044f\u043c.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("wndw_about_program", u"\u0412\u0435\u0440\u0441\u0438\u044f ver. 1.0.0.2024", None))
        self.pb_back.setText(QCoreApplication.translate("wndw_about_program", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

