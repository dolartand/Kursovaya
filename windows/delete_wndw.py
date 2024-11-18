# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_wndw.ui'
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

class Ui_wndw_delete(object):
    def setupUi(self, wndw_delete):
        if not wndw_delete.objectName():
            wndw_delete.setObjectName(u"wndw_delete")
        wndw_delete.resize(382, 210)
        wndw_delete.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_delete = QFrame(wndw_delete)
        self.frm_delete.setObjectName(u"frm_delete")
        self.frm_delete.setGeometry(QRect(20, 10, 341, 181))
        self.frm_delete.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_delete.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_delete.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_delete = QLabel(self.frm_delete)
        self.lbl_delete.setObjectName(u"lbl_delete")
        self.lbl_delete.setGeometry(QRect(0, 10, 341, 30))
        self.lbl_delete.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(20)
        self.lbl_delete.setFont(font)
        self.lbl_delete.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_delete.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_really_delete = QLabel(self.frm_delete)
        self.lbl_really_delete.setObjectName(u"lbl_really_delete")
        self.lbl_really_delete.setGeometry(QRect(10, 70, 321, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_really_delete.setFont(font1)
        self.lbl_really_delete.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.pb_yes = QPushButton(self.frm_delete)
        self.pb_yes.setObjectName(u"pb_yes")
        self.pb_yes.setGeometry(QRect(70, 120, 91, 34))
        font2 = QFont()
        font2.setPointSize(14)
        self.pb_yes.setFont(font2)
        self.pb_yes.setStyleSheet(u"QPushButton {\n"
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
        self.pb_no = QPushButton(self.frm_delete)
        self.pb_no.setObjectName(u"pb_no")
        self.pb_no.setGeometry(QRect(180, 120, 81, 34))
        self.pb_no.setFont(font2)
        self.pb_no.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(wndw_delete)

        QMetaObject.connectSlotsByName(wndw_delete)
    # setupUi

    def retranslateUi(self, wndw_delete):
        wndw_delete.setWindowTitle(QCoreApplication.translate("wndw_delete", u"Dialog", None))
        self.lbl_delete.setText(QCoreApplication.translate("wndw_delete", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.lbl_really_delete.setText(QCoreApplication.translate("wndw_delete", u"\u0412\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c?", None))
        self.pb_yes.setText(QCoreApplication.translate("wndw_delete", u"\u0414\u0430", None))
        self.pb_no.setText(QCoreApplication.translate("wndw_delete", u"\u041d\u0435\u0442", None))
    # retranslateUi

