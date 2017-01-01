from passlib.hash import sha256_crypt
import sqlite3
import re
from settings.general_settings import *
from queries.manage_db_queris import GET_PASS_BY_USER


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def encrypt(password):
    m = sha256_crypt.encrypt(password, rounds=100000, salt_size=8)
    return m


def verify(password, hash_pass):
    v = sha256_crypt.verify(password, hash_pass)
    return v


def validate_password(passwo):
    match = re.match('^.*(?=.{8,})(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', passwo)
    if match:
        return True
    return False


def check_pass(name, password):
    password_base = c.execute(GET_PASS_BY_USER, (name,))
    if password == password_base:
        return True
    else:
        return False
