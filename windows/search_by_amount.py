# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_by_amount_wndw.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_search_by_amount_wndw(object):
    def setupUi(self, search_by_amount_wndw):
        if not search_by_amount_wndw.objectName():
            search_by_amount_wndw.setObjectName(u"Поиск")
        search_by_amount_wndw.resize(400, 393)
        search_by_amount_wndw.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));\n"
"")
        self.frm_table_search_by_amount = QFrame(search_by_amount_wndw)
        self.frm_table_search_by_amount.setObjectName(u"frm_table_search_by_amount")
        self.frm_table_search_by_amount.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_amount.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.tv_search_by_amount = QTableView(self.frm_table_search_by_amount)
        self.tv_search_by_amount.setObjectName(u"tv_search_by_amount")
        self.tv_search_by_amount.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_amount.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.frm_search_by_amount = QFrame(search_by_amount_wndw)
        self.frm_search_by_amount.setObjectName(u"frm_search_by_amount")
        self.frm_search_by_amount.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_amount.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_amount.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_amount.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_search_by_amount = QLabel(self.frm_search_by_amount)
        self.lbl_search_by_amount.setObjectName(u"lbl_search_by_amount")
        self.lbl_search_by_amount.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_amount.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_amount.setFont(font)
        self.lbl_search_by_amount.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_search_by_amount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_enter_amount = QLabel(self.frm_search_by_amount)
        self.lbl_enter_amount.setObjectName(u"lbl_enter_amount")
        self.lbl_enter_amount.setGeometry(QRect(10, 50, 151, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_amount.setFont(font1)
        self.lbl_enter_amount.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.le_enter_amount = QLineEdit(self.frm_search_by_amount)
        self.le_enter_amount.setObjectName(u"le_enter_amount")
        self.le_enter_amount.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_amount.setFont(font1)
        self.pb_show = QPushButton(self.frm_search_by_amount)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(search_by_amount_wndw)

        QMetaObject.connectSlotsByName(search_by_amount_wndw)
    # setupUi

    def retranslateUi(self, search_by_amount_wndw):
        search_by_amount_wndw.setWindowTitle(QCoreApplication.translate("search_by_amount_wndw", u"Поиск", None))
        self.lbl_search_by_amount.setText(QCoreApplication.translate("search_by_amount_wndw", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043a\u043e\u043b-\u0432\u0443 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.lbl_enter_amount.setText(QCoreApplication.translate("search_by_amount_wndw", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e", None))
        self.pb_show.setText(QCoreApplication.translate("search_by_amount_wndw", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
    # retranslateUi

