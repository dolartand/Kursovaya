from windows import *
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem


class SearchByName(QDialog):
    def __init__(self, db):
        super(SearchByName, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_name()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv__search_by_name.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        name = self.ui.le_enter_name.text()
        items = self.db.search_by_name(name)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByType(QDialog):
    def __init__(self, db):
        super(SearchByType, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_type()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv_search_by_type.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        tech_type = self.ui.cb_type_tech.currentText()
        items = self.db.search_by_type(tech_type)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByYear(QDialog):
    def __init__(self, db):
        super(SearchByYear, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_year()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv_search_by_year.setModel(self.model)
        self.ui.pushButton.clicked.connect(self.show_results)

    def show_results(self):
        year = self.ui.le_enter_year.text()
        items = self.db.search_by_year(year)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByValue(QDialog):
    def __init__(self, db):
        super(SearchByValue, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_value()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv_search_by_value.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        price = self.ui.le_enter_value.text()
        items = self.db.search_by_price(price)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByAmount(QDialog):
    def __init__(self, db):
        super(SearchByAmount, self).__init__()
        self.db = db
        self.ui = Ui_search_by_amount_wndw()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv_search_by_amount.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        amount = self.ui.le_enter_amount.text()
        items = self.db.search_by_amount(amount)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByCondition(QDialog):
    def __init__(self, db):
        super(SearchByCondition, self).__init__()
        self.db = db
        self.ui = Ui_search_by_condition_wndw()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv_search_by_condition.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        condition = self.ui.cb_condition.currentText()
        items = self.db.search_by_condition(condition)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByNumberAud(QDialog):
    def __init__(self, db):
        super(SearchByNumberAud, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_numbe_aud()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv__search_by_number.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        number = self.ui.le_enter_number.text()
        items = self.db.search_by_number_aud(number)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))


class SearchByResponsible(QDialog):
    def __init__(self, db):
        super(SearchByResponsible, self).__init__()
        self.db = db
        self.ui = Ui_wndw_search_by_otvetstv()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.tv__search_by_otvetstv.setModel(self.model)
        self.ui.pb_show.clicked.connect(self.show_results)

    def show_results(self):
        fam = self.ui.le_enter_fam.text()
        items = self.db.search_by_responsible(fam)
        self.model.setRowCount(len(items))
        self.model.setColumnCount(9)
        headers = ['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние', 'Номер аудитории',
                   'Фамилия ответственного']
        self.model.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(items):
            for column, value in enumerate(item):
                self.model.setItem(row, column, QStandardItem(str(value)))
