# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_wndw.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_help_wndw(object):
    def setupUi(self, help_wndw):
        if not help_wndw.objectName():
            help_wndw.setObjectName(u"Помощь")
        help_wndw.resize(802, 468)
        help_wndw.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40)  \n"
"    );\n"
"\n"
"")
        self.frame = QFrame(help_wndw)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 451))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 50, 761, 341))
        self.textEdit.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.textEdit.setReadOnly(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 10, 111, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(290, 400, 181, 41))
        font1 = QFont()
        font1.setPointSize(12)
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

        self.retranslateUi(help_wndw)

        QMetaObject.connectSlotsByName(help_wndw)
    # setupUi

    def retranslateUi(self, help_wndw):
        help_wndw.setWindowTitle(QCoreApplication.translate("help_wndw", u"Помощь", None))
        self.textEdit.setHtml(QCoreApplication.translate("help_wndw", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434"
                        "\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438 \u043e \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0435. \u041e\u043d\u0430 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0443\u0434\u043e\u0431\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f, \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f, \u043f\u043e\u0438\u0441\u043a\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0430\u0440\u0445\u0438\u0432\u0443 \u0443\u0434\u0430\u043b\u0451"
                        "\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439. \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435 \u0438 \u0441\u0430\u043c\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435.</span></p>\n"
"<hr />\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438</span></h2>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">1. \u041e\u0442\u043e\u0431"
                        "\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043e \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0435</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442 \u0442\u0430\u0431\u043b\u0438\u0446\u0443, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u0438 \u043e \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0435.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u044b \u043f\u043e\u043b\u044f:\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID \u0437\u0430\u043f\u0438\u0441\u0438;</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f;</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0438\u043f \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438"
                        "\u044f (\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440, \u0432\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0430 \u0438 \u0442.\u0434.);</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430;</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c;</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u043e\u0441"
                        "\u0442\u043e\u044f\u043d\u0438\u0435 (\u0432 \u0440\u0430\u0431\u043e\u0442\u0435, \u0441\u043f\u0438\u0441\u0430\u043d\u0430, \u0432 \u0440\u0435\u043c\u043e\u043d\u0442\u0435)</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u043e\u043c\u0435\u0440 \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0441\u0432\u0435\u043d\u043d\u043e\u0433\u043e</li></ul></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">2. \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0437\u0430\u043f\u0438\u0441"
                        "\u0438</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u0441 \u043f\u043e\u043b\u044f\u043c\u0438 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 (\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435, \u0442\u0438\u043f \u0438 \u0442.\u0434.).</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u043f\u043e\u043b\u044f.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c&quot;</span>, \u0447\u0442\u043e\u0431\u044b \u043d\u043e"
                        "\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u043b\u0430\u0441\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">3. \u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px;"
                        " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u0441\u0442\u0440\u043e\u043a\u0443 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0430\u043f\u0438\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0443\u0434\u0430\u043b\u0435\u043d\u0430 \u0438\u0437 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0438 \u043f\u0435\u0440\u0435\u043c\u0435\u0449"
                        "\u0435\u043d\u0430 \u0432 \u0430\u0440\u0445\u0438\u0432.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">4. \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u0441\u0442\u0440\u043e\u043a\u0443 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0435\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u044b\u0431"
                        "\u0440\u0430\u043d\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u043d\u0435\u0441\u0438\u0442\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432 \u043f\u043e\u043b\u044f.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c&quot;</span>, \u0447\u0442\u043e\u0431\u044b \u043e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:12pt; font-weight:700;\">5. \u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0438</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0437\u0430\u043f\u0438\u0441\u0438:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u043f\u043e\u0438\u0441\u043a\u0430, \u043e\u0442\u043c\u0435\u0442\u0438\u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438"
                        "\u0439 \u0440\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u043e\u0439 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, &quot;\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e&quot;, &quot;\u041f\u043e \u0442\u0438\u043f\u0443 \u0442\u0435\u0445\u043d\u0438\u043a\u0438&quot;, &quot;\u041f\u043e \u0446\u0435\u043d\u0435&quot;).</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0418\u0441\u043a\u0430\u0442\u044c&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u043f\u043e\u0438\u0441\u043a\u0430.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043b\u0438 \u0446\u0435\u043d\u0443).</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0412\u044b\u0432\u0435\u0441\u0442\u0438&quot;</span>, \u0447\u0442\u043e\u0431\u044b \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:12pt; font-weight:700;\">6. \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u041e\u0431"
                        " \u0430\u0432\u0442\u043e\u0440\u0435&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u043e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435 \u0440\u0430\u0431\u043e\u0442\u044b.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">7. \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\">\u0414\u043b\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u043e\u043a\u043d\u043e \u0441 \u043a\u0440\u0430\u0442\u043a\u0438\u043c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u043c \u043f\u0440\u043e"
                        "\u0433\u0440\u0430\u043c\u043c\u044b, \u0432\u0435\u0440\u0441\u0438\u0435\u0439.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">8. \u041e\u0442\u043a\u0440\u044b\u0442\u0438\u0435 \u0430\u0440\u0445\u0438\u0432\u0430 \u0437\u0430\u043f\u0438\u0441\u0435\u0439</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0430\u0440\u0445\u0438\u0432\u0430:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0430\u0440\u0445\u0438\u0432&quot;</span>.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0435\u0442\u0441\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u044b\u043b\u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u044b \u0438\u0437 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u044b.</li></ol></li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">9"
                        ". \u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b:\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:700;\">&quot;\u0412\u044b\u0445\u043e\u0434&quot;</span>.</li>\n"
"<li style=\" font-size:12"
                        "pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u0442 \u0440\u0430\u0431\u043e\u0442\u0443.</li></ol></li></ul>\n"
"<hr />\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u044f</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0441\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f (\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435, \u0440\u0435\u0434\u0430"
                        "\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435) \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u044e\u0442\u0441\u044f \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0430\u0440\u0445\u0438\u0432\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b \u0434\u043b\u044f \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f, \u043d\u043e \u043d\u0435 \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u041f"
                        "\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0414\u043b\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u0435\u0441\u044c \u043a \u0430\u0432\u0442\u043e\u0440\u0443 \u0447\u0435\u0440\u0435\u0437 \u043e\u043a\u043d\u043e </span><span style=\" font-size:12pt; font-weight:700;\">&quot;\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435&quot;</span><span style=\" font-size:12pt;\">, \u0433\u0434\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("help_wndw", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.pb_exit.setText(QCoreApplication.translate("help_wndw", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

