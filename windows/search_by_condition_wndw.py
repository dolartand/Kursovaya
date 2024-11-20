# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_by_condition_wndw.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_search_by_condition_wndw(object):
    def setupUi(self, search_by_condition_wndw):
        if not search_by_condition_wndw.objectName():
            search_by_condition_wndw.setObjectName(u"Поиск")
        search_by_condition_wndw.resize(400, 394)
        search_by_condition_wndw.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_search_by_condition = QFrame(search_by_condition_wndw)
        self.frm_search_by_condition.setObjectName(u"frm_search_by_condition")
        self.frm_search_by_condition.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_condition.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_condition.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_search_by_condition = QLabel(self.frm_search_by_condition)
        self.lbl_search_by_condition.setObjectName(u"lbl_search_by_condition")
        self.lbl_search_by_condition.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_condition.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_condition.setFont(font)
        self.lbl_search_by_condition.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_search_by_condition.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_enter_condition = QLabel(self.frm_search_by_condition)
        self.lbl_enter_condition.setObjectName(u"lbl_enter_condition")
        self.lbl_enter_condition.setGeometry(QRect(10, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_condition.setFont(font1)
        self.lbl_enter_condition.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.pb_show = QPushButton(self.frm_search_by_condition)
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
        self.cb_condition = QComboBox(self.frm_search_by_condition)
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.setObjectName(u"cb_condition")
        self.cb_condition.setGeometry(QRect(180, 40, 191, 31))
        self.cb_condition.setFont(font)
        self.frm_table_search_by_condition = QFrame(search_by_condition_wndw)
        self.frm_table_search_by_condition.setObjectName(u"frm_table_search_by_condition")
        self.frm_table_search_by_condition.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_condition.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_condition.setFrameShadow(QFrame.Shadow.Raised)
        self.tv_search_by_condition = QTableView(self.frm_table_search_by_condition)
        self.tv_search_by_condition.setObjectName(u"tv_search_by_condition")
        self.tv_search_by_condition.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_condition.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        self.retranslateUi(search_by_condition_wndw)

        QMetaObject.connectSlotsByName(search_by_condition_wndw)
    # setupUi

    def retranslateUi(self, search_by_condition_wndw):
        search_by_condition_wndw.setWindowTitle(QCoreApplication.translate("search_by_condition_wndw", u"Поиск", None))
        self.lbl_search_by_condition.setText(QCoreApplication.translate("search_by_condition_wndw", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044e \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.lbl_enter_condition.setText(QCoreApplication.translate("search_by_condition_wndw", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.pb_show.setText(QCoreApplication.translate("search_by_condition_wndw", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
        self.cb_condition.setItemText(0, QCoreApplication.translate("search_by_condition_wndw", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.cb_condition.setItemText(1, QCoreApplication.translate("search_by_condition_wndw", u"\u0412 \u0440\u0435\u043c\u043e\u043d\u0442\u0435", None))
        self.cb_condition.setItemText(2, QCoreApplication.translate("search_by_condition_wndw", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0430", None))

    # retranslateUi

