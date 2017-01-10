import sqlite3
from client import Client
from settings import DB_NAME


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def change_message(new_message, logged_user):
    cursor.execute(SET_CLIENT_MESSAGE)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(SET_CLIENT_PASSWORD)
    conn.commit()


def register(username, password):
    cursor.execute(INSERT_INTO_CLIENT)
    conn.commit()


def login(username, password):
    cursor.execute(GET_CLIENT_FROM_DB)
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
