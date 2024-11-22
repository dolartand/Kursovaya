from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QComboBox, QTableView


class Ui_wndw_search_by_type(object):
    def setupUi(self, wndw_search_by_type):
        """
        Method to set up the UI for the window searching by type of technology.
        """
        if not wndw_search_by_type.objectName():
            wndw_search_by_type.setObjectName(u"Поиск")

        # Set window size and style
        wndw_search_by_type.resize(400, 429)
        wndw_search_by_type.setStyleSheet(u"background-color: qlineargradient(\n"
                                          "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                          "        stop:0 rgba(139,0,255, 20), \n"
                                          "        stop:1 rgba(115,102,189, 40));")

        # Frame for the search results
        self.frm_table_search_by_type = QFrame(wndw_search_by_type)
        self.frm_table_search_by_type.setObjectName(u"frm_table_search_by_type")
        self.frm_table_search_by_type.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_type.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_type.setFrameShadow(QFrame.Shadow.Raised)

        # Table for displaying search results
        self.tv_search_by_type = QTableView(self.frm_table_search_by_type)
        self.tv_search_by_type.setObjectName(u"tv_search_by_type")
        self.tv_search_by_type.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Frame for the search input
        self.frm_search_by_type = QFrame(wndw_search_by_type)
        self.frm_search_by_type.setObjectName(u"frm_search_by_type")
        self.frm_search_by_type.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_type.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_type.setFrameShadow(QFrame.Shadow.Raised)

        # Label for search header
        self.lbl_search_by_type = QLabel(self.frm_search_by_type)
        self.lbl_search_by_type.setObjectName(u"lbl_search_by_type")
        self.lbl_search_by_type.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_type.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_type.setFont(font)
        self.lbl_search_by_type.setStyleSheet(u"background-color: none;\n"
                                              "border: none;")
        self.lbl_search_by_type.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label for selecting technology type
        self.lbl_enter_type = QLabel(self.frm_search_by_type)
        self.lbl_enter_type.setObjectName(u"lbl_enter_type")
        self.lbl_enter_type.setGeometry(QRect(0, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_type.setFont(font1)
        self.lbl_enter_type.setStyleSheet(u"background-color: none;\n"
                                          "border:none;")

        # Button to show results
        self.pb_show = QPushButton(self.frm_search_by_type)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
                                   "color: white;\n"
                                   "background-color: rgba(254,254,34, 30);\n"
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

        # ComboBox for selecting technology type
        self.cb_type_tech = QComboBox(self.frm_search_by_type)
        self.cb_type_tech.setObjectName(u"cb_type_tech")
        self.cb_type_tech.setGeometry(QRect(180, 40, 191, 31))
        self.cb_type_tech.setFont(font)

        # Populate ComboBox with items
        self.cb_type_tech.addItems([
            QCoreApplication.translate("wndw_search_by_type", u"Процессор", None),
            QCoreApplication.translate("wndw_search_by_type", u"Материнская плата", None),
            QCoreApplication.translate("wndw_search_by_type", u"Видеокарта", None),
            QCoreApplication.translate("wndw_search_by_type", u"Оперативная память", None),
            QCoreApplication.translate("wndw_search_by_type", u"SSD", None),
            QCoreApplication.translate("wndw_search_by_type", u"Жёсткий диск", None),
            QCoreApplication.translate("wndw_search_by_type", u"Блок питания", None),
            QCoreApplication.translate("wndw_search_by_type", u"Корпус", None),
        ])

        # Call method to set text for UI elements
        self.retranslateUi(wndw_search_by_type)

        # Connect slots and signals
        QMetaObject.connectSlotsByName(wndw_search_by_type)

    def retranslateUi(self, wndw_search_by_type):
        """
        Method to set text for UI elements.
        """
        wndw_search_by_type.setWindowTitle(QCoreApplication.translate("wndw_search_by_type", u"Поиск", None))
        self.lbl_search_by_type.setText(
            QCoreApplication.translate("wndw_search_by_type", u"Поиск по типу техники", None))
        self.lbl_enter_type.setText(QCoreApplication.translate("wndw_search_by_type", u"Выберите тип техники", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_type", u"Вывести", None))