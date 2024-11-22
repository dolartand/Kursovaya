from PySide6.QtWidgets import QMainWindow
from windows import *
from database import ArchiveDatabase


class AddNote(QMainWindow):
    """
    Окно добавления записи

    Функционал:
    Добавление новой записи в базу данных
    """
    def __init__(self, db, update_table_callback):
        super(AddNote, self).__init__()
        self.db = db
        self.update_table_callback = update_table_callback
        self.ui = Ui_wndw_add()
        self.ui.setupUi(self)

        self.ui.pb_add.clicked.connect(self.add_note)

    # Добавление записи
    def add_note(self):
        name = self.ui.le_name.text()
        item_type = self.ui.cb_add_type.currentText()
        year = int(self.ui.le_year.text().strip())
        price = float(self.ui.le_value.text())
        amount = int(self.ui.le_amount.text())
        condition = self.ui.cb_add_sost.currentText()
        number_aud = int(self.ui.le_number_aud.text())
        responsible = self.ui.le_otvetstv.text()

        self.db.add_item(name, item_type, year, price, amount, condition, number_aud, responsible)

        self.close()

        self.update_table_callback()


class DeleteNote(QMainWindow):
    """
    Окно подтверждения удаления записи

    Функционал:
    Открытие окна для подтверждения удаления записи из базы данных
    """
    def __init__(self, db, update_table_callback, item_id=None):
        super(DeleteNote, self).__init__()
        self.db = db
        self.item_id = item_id
        self.update_table_callback = update_table_callback
        self.ui = Ui_wndw_delete()
        self.ui.setupUi(self)

        self.ui.pb_yes.clicked.connect(self.confirm_delete)
        self.ui.pb_no.clicked.connect(self.close_delete)

    # Подтверждение удаления записи
    def confirm_delete(self):
        if self.item_id is not None:
            self.archive_db = ArchiveDatabase("databases/archive.db")
            self.archive_db.transfer_item(self.db, self.item_id)
            self.close()
            self.update_table_callback()

    # Закрытие окна
    def close_delete(self):
        self.close()


class EditNote(QMainWindow):
    """
    Окно редактирования записи

    Функционал:
    Загрузка данных выбранной записи для редактирования
    Сохранение изменений в базе данных
    """
    def __init__(self, db, update_table_callback):
        super(EditNote, self).__init__()
        self.db = db
        self.update_table_callback = update_table_callback
        self.ui = Ui_wndw_edit()
        self.ui.setupUi(self)

        self.ui.pb_save.clicked.connect(self.save_changes)

    # Загрузка данных выбранной записи
    def load_current_data(self, item_id):
        self.id = item_id
        item = self.db.fetch_item_by_id(item_id)
        if item:
            self.ui.le_name.setText(item[1])
            self.ui.cb_type_tech.setCurrentText(item[2])
            self.ui.le_year.setText(str(item[3]))
            self.ui.le_value.setText(str(item[4]))
            self.ui.le_amount.setText(str(item[5]))
            self.ui.cb_add_sost.setCurrentText(item[6])
            self.ui.le_number_aud.setText(str(item[7]))
            self.ui.le_otvetstv.setText(item[8])

    # Сохранение изменений
    def save_changes(self):
        name = self.ui.le_name.text()
        item_type = self.ui.cb_type_tech.currentText()
        year = int(self.ui.le_year.text())
        value = float(self.ui.le_value.text())
        amount = int(self.ui.le_amount.text())
        condition = self.ui.cb_add_sost.currentText()
        number_aud = int(self.ui.le_number_aud.text())
        responsible = self.ui.le_otvetstv.text()

        self.db.update_item(self.id, name, item_type, year, value, amount, condition, number_aud, responsible)
        self.close()
        self.update_table_callback()