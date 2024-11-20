# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_author_wndw.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_wndw_about_author(object):
    def setupUi(self, wndw_about_author):
        if not wndw_about_author.objectName():
            wndw_about_author.setObjectName(u"Об авторе")
        wndw_about_author.resize(400, 528)
        wndw_about_author.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frame = QFrame(wndw_about_author)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 381, 511))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 361, 291))
        self.label.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label.setPixmap(QPixmap(u"resourses/author_image.jpg"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 300, 71, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 340, 251, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 380, 271, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 420, 211, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.pb_back = QPushButton(self.frame)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setGeometry(QRect(20, 460, 341, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.pb_back.setFont(font2)
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
        self.pb_back.setFlat(False)

        self.retranslateUi(wndw_about_author)

        self.pb_back.setDefault(False)


        QMetaObject.connectSlotsByName(wndw_about_author)
    # setupUi

    def retranslateUi(self, wndw_about_author):
        wndw_about_author.setWindowTitle(QCoreApplication.translate("wndw_about_author", u"Об авторе", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("wndw_about_author", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_3.setText(QCoreApplication.translate("wndw_about_author", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442 \u0433\u0440\u0443\u043f\u043f\u044b 10701323", None))
        self.label_4.setText(QCoreApplication.translate("wndw_about_author", u"\u0414\u043e\u043b\u0435\u043d\u043a\u043e \u0410\u0440\u0442\u0443\u0440 \u0410\u043d\u0434\u0440\u0435\u0435\u0432\u0438\u0447", None))
        self.label_5.setText(QCoreApplication.translate("wndw_about_author", u"dolartand@gmail.com", None))
        self.pb_back.setText(QCoreApplication.translate("wndw_about_author", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

