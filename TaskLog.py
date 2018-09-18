import sqlite3


class TaskLog:
    __db_path = "DB/HomeEvents.db"
    __tasks = []

    def __init__(self, db_path = None):
        if db_path:
            self.__db_path = db_path

    def load_data(self):
        db = sqlite3.connect(self.__db_path)
        cursor = db.cursor()

        cursor.execute("""
        SELECT * 
        FROM TaskLog
        """)

        self.__tasks = cursor.fetchall()



