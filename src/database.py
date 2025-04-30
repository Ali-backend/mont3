import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    genre TEXT,
                    year TEXT
                )
                """
            )
            conn.commit()

 
    def add_movie(self, title: str, genre: str, year: str):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)",
                (title, genre, year),
            )
            conn.commit()

    def get_all_movies(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies")
            return cursor.fetchall()

  
    def delete_movie(self, movie_id: int):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            conn.commit()
