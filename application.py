from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from search import *
from database import Database
from note_operations import *
from about_windows import *


class Archive(QMainWindow):
    def __init__(self, item_id=None):
        super(Archive, self).__init__()
        self.item_id = item_id
        self.db = ArchiveDatabase("databases/archive.db")
        self.ui = Ui_wndw_archive()
        self.ui.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние',
                                              'Номер аудитории', 'Фамилия ответственного'])
        self.ui.tv_archive.setModel(self.model)

        self.ui.tv_archive.setSortingEnabled(True)
        self.ui.tv_archive.setColumnWidth(0, 15)
        self.ui.tv_archive.setColumnWidth(3, 50)
        self.ui.tv_archive.setColumnWidth(5, 50)
        self.ui.tv_archive.setColumnWidth(7, 120)
        self.ui.tv_archive.setColumnWidth(8, 150)
        self.ui.tv_archive.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        self.ui.pb_exit.clicked.connect(self.close)
        self.ui.pb_delete.clicked.connect(self.delete_from_archive)

        self.load_archive()

    def load_archive(self):
        self.model.removeRows(0, self.model.rowCount())
        items = self.db.fetch_all_items()

        for item in items:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(item[1]),
                QStandardItem(item[2]),
                QStandardItem(str(item[3])),
                QStandardItem(str(item[4])),
                QStandardItem(str(item[5])),
                QStandardItem(item[6]),
                QStandardItem(str(item[7])),
                QStandardItem(item[8])
            ]
            self.model.appendRow(row)

    def delete_from_archive(self):
        selected_indexes = self.ui.tv_archive.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Удаление записи", "Пожалуйста, выберите запись для удаления.")
            return

        selected_row = selected_indexes[0].row()
        item_id = int(self.model.item(selected_row, 0).text())

        confirmation = QMessageBox.question(self, "Подтверждение удаления",
                                            f"Вы уверены, что хотите удалить запись с ID {item_id}?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.delete_item(item_id)
            self.model.removeRow(selected_row)


class TechBook(QMainWindow):
    def __init__(self):
        super(TechBook, self).__init__()
        self.db = Database("databases/tech_book.db")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = QStandardItemModel()
        self.ui.tv_main_table.setModel(self.model)
        self.model.setHorizontalHeaderLabels(['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние',
                                              'Номер аудитории', 'Фамилия ответственного'])

        self.ui.tv_main_table.setSortingEnabled(True)
        self.ui.tv_main_table.setColumnWidth(0, 15)
        self.ui.tv_main_table.setColumnWidth(3, 50)
        self.ui.tv_main_table.setColumnWidth(5, 50)
        self.ui.tv_main_table.setColumnWidth(7, 120)
        self.ui.tv_main_table.setColumnWidth(8, 150)
        self.ui.tv_main_table.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        self.ui.pb_add.clicked.connect(self.open_add_window)
        self.ui.pb_delete.clicked.connect(self.open_delete_window)
        self.ui.pb_edit.clicked.connect(self.open_edit_window)
        self.ui.pb_search.clicked.connect(self.open_search_window)
        self.ui.pb_show_archive.clicked.connect(self.open_archive_window)
        self.ui.pb_about_author.clicked.connect(self.open_about_author_window)
        self.ui.pb_about_program.clicked.connect(self.open_about_program_window)
        self.ui.pb_exit.clicked.connect(self.close)

        self.ui.add_action.triggered.connect(self.open_add_window)
        self.ui.delete_action.triggered.connect(self.open_delete_window)
        self.ui.edit_action.triggered.connect(self.open_edit_window)
        self.ui.archive_action.triggered.connect(self.open_archive_window)
        self.ui.about_author_action.triggered.connect(self.open_about_author_window)
        self.ui.about_program_action.triggered.connect(self.open_about_program_window)
        self.ui.help_action.triggered.connect(self.open_help_window)
        self.ui.exit_action.triggered.connect(self.close)

        self.load_data()

    def open_search_window(self):
        if self.ui.rb_name.isChecked():
            self.search_window = SearchByName(self.db)
        elif self.ui.rb_type.isChecked():
            self.search_window = SearchByType(self.db)
        elif self.ui.rb_year.isChecked():
            self.search_window = SearchByYear(self.db)
        elif self.ui.rb_value.isChecked():
            self.search_window = SearchByValue(self.db)
        elif self.ui.rb_amount.isChecked():
            self.search_window = SearchByAmount(self.db)
        elif self.ui.rb_condition.isChecked():
            self.search_window = SearchByCondition(self.db)
        elif self.ui.rb_number_aud.isChecked():
            self.search_window = SearchByNumberAud(self.db)
        elif self.ui.rb_otvetstv.isChecked():
            self.search_window = SearchByResponsible(self.db)

        self.search_window.show()

    def open_add_window(self):
        self.add_window = AddNote(self.db, self.load_data)
        self.add_window.show()

    def open_delete_window(self):
        selected_row = self.ui.tv_main_table.currentIndex()
        if selected_row.isValid():
            item_id = int(self.model.item(selected_row.row(), 0).text())
            self.delete_window = DeleteNote(self.db, self.load_data, item_id)
            self.delete_window.show()

    def open_edit_window(self):
        selected_index = self.ui.tv_main_table.currentIndex()
        if selected_index.isValid():
            id = int(self.model.item(selected_index.row(), 0).text())
            self.edit_window = EditNote(self.db, self.load_data)
            self.edit_window.load_current_data(id)
            self.edit_window.show()

    def open_archive_window(self):
        self.archive_window = Archive(self.load_data)
        self.archive_window.show()

    def open_about_author_window(self):
        self.author_window = AboutAuthor()
        self.author_window.show()

    def open_about_program_window(self):
        self.program_window = AboutProgram()
        self.program_window.show()

    def open_help_window(self):
        self.help_window = Help()
        self.help_window.show()

    def load_data(self):
        self.model.removeRows(0, self.model.rowCount())

        items = self.db.fetch_all_items()

        for item in items:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(item[1]),
                QStandardItem(item[2]),
                QStandardItem(str(item[3])),
                QStandardItem(str(item[4])),
                QStandardItem(str(item[5])),
                QStandardItem(item[6]),
                QStandardItem(str(item[7])),
                QStandardItem(item[8])
            ]
            self.model.appendRow(row)
