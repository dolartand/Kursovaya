# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archive_wndw.ui'
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
    QLabel, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_wndw_archive(object):
    def setupUi(self, wndw_archive):
        if not wndw_archive.objectName():
            wndw_archive.setObjectName(u"wndw_archive")
        wndw_archive.resize(801, 467)
        wndw_archive.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frame = QFrame(wndw_archive)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 451))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_archive = QLabel(self.frame)
        self.lbl_archive.setObjectName(u"lbl_archive")
        self.lbl_archive.setGeometry(QRect(200, 0, 341, 41))
        self.lbl_archive.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_archive.setFont(font)
        self.lbl_archive.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_archive.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tv_archive = QTableView(self.frame)
        self.tv_archive.setObjectName(u"tv_archive")
        self.tv_archive.setGeometry(QRect(10, 60, 751, 311))
        self.tv_archive.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.pb_delete = QPushButton(self.frame)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setGeometry(QRect(10, 390, 135, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.pb_delete.setFont(font1)
        self.pb_delete.setStyleSheet(u"QPushButton {\n"
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
        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(160, 390, 131, 41))
        self.pb_exit.setFont(font1)
        self.pb_exit.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(wndw_archive)

        QMetaObject.connectSlotsByName(wndw_archive)
    # setupUi

    def retranslateUi(self, wndw_archive):
        wndw_archive.setWindowTitle(QCoreApplication.translate("wndw_archive", u"Dialog", None))
        self.lbl_archive.setText(QCoreApplication.translate("wndw_archive", u"\u0410\u0440\u0445\u0438\u0432 \u0443\u0434\u0430\u043b\u0451\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.pb_delete.setText(QCoreApplication.translate("wndw_archive", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pb_exit.setText(QCoreApplication.translate("wndw_archive", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

