import sqlite3
from client import Client
from settings import DB_NAME
from validators import validate_pass
from queries import *


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def change_message(new_message, logged_user):
    cursor.execute(SET_CLIENT_MESSAGE)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(SET_CLIENT_PASSWORD)
    conn.commit()


# @encrypt_pass()
@validate_pass()
def set_pass(password):
    return password


def register(username, password):
    password = set_pass(password)
    cursor.execute(INSERT_INTO_CLIENT, (username, password))
    conn.commit()


def get_user(username, password):
    cursor.execute(GET_CLIENT_FROM_DB, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
