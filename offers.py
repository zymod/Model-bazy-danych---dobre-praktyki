import sqlite3
import sys
import os
from sqlite3 import connect


class OffersDatabase(object):
    def __init__(self):
        db_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'offers')
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
        db_path = os.path.join(db_dir, 'offers.sqlite3')
        self.conn = sqlite3.connection(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.db_name},)"

    def __str__(self):
        return f"{self.__class__.__name__} {self.db_name}"

    def close(self):
        self.conn.close()


    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS offers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                offer_id TEXT
                )
            """
        try:
            with self.conn, self.conn.cursor() as cursor:
                cursor.execute(query)
        except sqlite3.DatabaseError as e:
            print("Wystąpił błąd przy tworzeniu tabeli: ", e)
        

        try:
            self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS offers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                offer_id TEXT
                )
            """)
        except sqlite3.Error as error:
            print("error occurred: ", error)


    def insert_offer(self, offer_id):
        query = "INSERT INTO offers (offer_id) VALUES(?)"
        try:
            with self.conn, self.conn.cursor() as cursor:
                cursor.execute(query, (str(offer_id),))
        except sqlite3.DatabaseError as e:
            print("Wystąpił błąd przy dodawaniu oferty: ", e)


    def select_offer(self, offer_id):
        query = "SELECT * FROM offers WHERE offer_id=?"
        try:
            with self.conn, self.conn.cursor() as cursor:
                cursor.execute(query, (str(offer_id),))
                result = cursor.fetchone()
        except sqlite3.DatabaseError as e:
            print("Wystąpił błąd przy pobieraniu danych: ", e)
            result = None
        return result


    def get_all_fields(self):
        query = "SELECT * FROM offers"
        try:
            with self.conn, self.conn.cursor() as cursor:
                cursor.execute(query)
                result = cursot.fetchall()
        except sqlite3.DatabaseError as e:
            print("Wystąpił błąd przy pobieraniu danych: ", e)
            result = None
        return result
