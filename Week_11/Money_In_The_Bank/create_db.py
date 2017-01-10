import sqlite3
from settings import DB_NAME
from queries import CREATE_CLIENT_TABLE, DROP_CLIENT_TABLE


connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def create_database():
    cursor.execute(CREATE_CLIENT_TABLE)
    connection.commit()


def drop_database_tables():
    cursor.execute(DROP_CLIENT_TABLE)
    connection.commit()


def main():
    drop_database_tables()
    create_database()


if __name__ == '__main__':
    main()
