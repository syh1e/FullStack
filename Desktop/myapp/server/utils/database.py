import mysql.connector
from mysql.connector import Error
from typing import Optional

class DatabaseConnection:
    _instance: Optional['DatabaseConnection'] = None
    _connection = None
    _cursor = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._connection is None:
            self.connect()

    def connect(self):
        try:
            self._connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='study_db'
            )
            self._cursor = self._connection.cursor(dictionary=True)
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    @property
    def connection(self):
        if not self._connection or not self._connection.is_connected():
            self.connect()
        return self._connection

    @property
    def cursor(self):
        if not self._cursor or not self._connection.is_connected():
            self.connect()
        return self._cursor

    def execute(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor
        except Error as e:
            self.connection.rollback()
            print(f"Error executing query: {e}")
            raise

    def fetch_one(self, query: str, params: tuple = None):
        cursor = self.execute(query, params)
        return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = None):
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
        self._cursor = None
        self._connection = None 