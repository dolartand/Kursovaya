import sqlite3


class Database:
    """
    Класс для работы с основной базой данных

    Функционал:
    Создание таблицы.
    Добавление.
    Удаление.
    Обновление.
    Поиск.
    Получение данных из базы данных.
    """

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    # Создание таблицы
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            type TEXT NOT NULL,
                            year INTEGER NOT NULL,
                            price FLOAT NOT NULL,
                            amount INTEGER NOT NULL,
                            condition TEXT NOT NULL,
                            number_aud INTEGER NOT NULL,
                            responsible TEXT NOT NULL)''')
        self.conn.commit()

    # Добавление записи
    def add_item(self, name, item_type, year, price, amount, condition, number_aud, responsible):
        self.cursor.execute("SELECT MAX(id) FROM items")
        max_id = self.cursor.fetchone()[0]
        if max_id is None:
            new_id = 1
        else:
            new_id = max_id + 1
        self.cursor.execute('''INSERT INTO items (id, name, type, year, price, amount, condition, number_aud, 
                                                        responsible) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (new_id, name, item_type, year, price,
                                                                       amount, condition, number_aud, responsible))
        self.conn.commit()

    # Удаление записи
    def delete_item(self, item_id):
        self.cursor.execute('''DELETE FROM items WHERE id = ?''', (item_id,))
        self.conn.commit()

    # Редактирование записи
    def update_item(self, item_id, name=None, item_type=None, year=None, price=None, amount=None,
                    condition=None, number_aud=None, responsible=None):
        if name:
            self.cursor.execute('''UPDATE items SET name = ? WHERE id = ?''', (name, item_id))
        if item_type:
            self.cursor.execute('''UPDATE items SET type = ? WHERE id = ?''', (item_type, item_id))
        if year:
            self.cursor.execute('''UPDATE items SET year = ? WHERE id = ?''', (year, item_id))
        if price:
            self.cursor.execute('''UPDATE items SET price = ? WHERE id = ?''', (price, item_id))
        if amount:
            self.cursor.execute('''UPDATE items SET amount = ? WHERE id = ?''', (amount, item_id))
        if condition:
            self.cursor.execute('''UPDATE items SET condition = ? WHERE id = ?''', (condition, item_id))
        if number_aud:
            self.cursor.execute('''UPDATE items SET number_aud = ? WHERE id = ?''', (number_aud, item_id))
        if responsible:
            self.cursor.execute('''UPDATE items SET responsible = ? WHERE id = ?''', (responsible, item_id))
        self.conn.commit()

    # Поиск записи по имени
    def search_by_name(self, name):
        self.cursor.execute('''SELECT * FROM items WHERE name LIKE ?''', ('%' + name + '%',))
        return self.cursor.fetchall()

    # Поиск записи по типу техники
    def search_by_type(self, type):
        self.cursor.execute('''SELECT * FROM items WHERE type LIKE ?''', ('%' + type + '%',))
        return self.cursor.fetchall()

    # Поиск записи по году выпуска
    def search_by_year(self, year):
        self.cursor.execute('''SELECT * FROM items WHERE year LIKE ?''', ('%' + year + '%',))
        return self.cursor.fetchall()

    # Поиск записи по цене
    def search_by_price(self, price):
        self.cursor.execute('''SELECT * FROM items WHERE price LIKE ?''', ('%' + price + '%',))
        return self.cursor.fetchall()

    # Поиск записи по количеству на складе
    def search_by_amount(self, amount):
        self.cursor.execute('''SELECT * FROM items WHERE amount LIKE ?''', ('%' + amount + '%',))
        return self.cursor.fetchall()

    # Поиск записи по состоянию техники (списана, в работе, в ремонте)
    def search_by_condition(self, cond):
        self.cursor.execute('''SELECT * FROM items WHERE condition LIKE ?''', ('%' + cond + '%',))
        return self.cursor.fetchall()

    # Поиск записи по номеру аудитории
    def search_by_number_aud(self, number):
        self.cursor.execute('''SELECT * FROM items WHERE number_aud LIKE ?''', ('%' + number + '%',))
        return self.cursor.fetchall()

    # Поиск записи по фамилии ответственного
    def search_by_responsible(self, resp):
        self.cursor.execute('''SELECT * FROM items WHERE responsible LIKE ?''', ('%' + resp + '%',))
        return self.cursor.fetchall()

    # Получение всех записей
    def fetch_all_items(self):
        self.cursor.execute('''SELECT * FROM items''')
        return self.cursor.fetchall()

    # Получение записи по id
    def fetch_item_by_id(self, item_id):
        self.cursor.execute('''SELECT * FROM items WHERE id = ?''', (item_id,))
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()


class ArchiveDatabase:
    """
    Класс для работы с архивной базой данных.

    Функционал:
    Создание таблицы.
    Перенос записи из основной базы данных в архив.
    Удаление записи из архива.
    Получение данных из архива.
    """
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_archive()

    # Создание таблицы
    def create_archive(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS archive (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            type TEXT NOT NULL,
                            year INTEGER NOT NULL,
                            price FLOAT NOT NULL,
                            amount INTEGER NOT NULL,
                            condition TEXT NOT NULL,
                            number_aud INTEGER NOT NULL,
                            responsible TEXT NOT NULL)''')
        self.conn.commit()

    # Перенос записи из основной базы данных в архив
    def transfer_item(self, database: Database, item_id):
        try:
            with self.conn:
                item = database.fetch_item_by_id(item_id)
                if item:
                    self.cursor.execute('''INSERT INTO archive (name, type, year, price, amount, 
                                                                condition, number_aud, responsible)
                                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', item[1:])
                    database.delete_item(item_id)
                else:
                    raise ValueError(f"Item with id {item_id} not found in database.")
        except Exception as e:
            print(f"Failed to transfer item with id {item_id}: {e}")
            self.conn.rollback()

    # Удаление записи из архива
    def delete_item(self, item_id):
        self.cursor.execute('''DELETE FROM archive WHERE id = ?''', (item_id,))
        self.conn.commit()

    # Получение всех записей
    def fetch_all_items(self):
        self.cursor.execute('''SELECT * FROM archive''')
        return self.cursor.fetchall()

    # Получение записи по id
    def fetch_item_by_id(self, item_id):
        self.cursor.execute('''SELECT * FROM archive WHERE id = ?''', (item_id,))
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()
