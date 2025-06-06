import sqlite3


# CRUD - Create, Read, Update, Delete


class Database:
    def __init__(self, path: str):
        self.path = path

    # создание таблиц, если они не существуют
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    todo TEXT,
                    category TEXT
                )
                """
            )
            conn.commit()

    # добавление задачи(todo) в таблицу todos
    def add_todo(self, todo: str, category: str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO todos (todo, category) VALUES (?, ?)
                """,
                (todo, category),
            )
            conn.commit()

    # получение всех задач из таблицы todos
    def all_todos(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todos")
            # возвращает список кортежей!
            return cursor.fetchall()

    def get_one_todo(self, todo_id: str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todos WHERE id=?", (todo_id,))
            return cursor.fetchone()

    def delete_todo(self, todo_id: int):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
            conn.commit()

    # database.update(todo_id=2, todo="do Math hw", category="school")
    def update_todo(self, todo_id: int, todo: str, category: str):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "UPDATE todos SET todo=?, category=? WHERE id=?",
                (todo, category, todo_id),
            )
            conn.commit()

