import sqlite3
from settings.general_settings import *
from user_interface.validators import encrypt
from queries.create_db_queries import INSERT_INTO_USER


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


class CinemaUser:
    def __init__(self, username, password):
        self.username = username
        self.password = encrypt(password)

    def save(self):
        user = [(self.username, self.password)]
        c.executemany(INSERT_INTO_USER, user)
        db.commit()
