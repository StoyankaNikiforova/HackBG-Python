import sqlite3
# import hashlib

from settings.general_settings import DB_NAME
from create_db_queries import *


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def create_database():
    c.execute(CREATE_MOVIE_TABLE)
    c.execute(CREATE_PROJECTION_TABLE)
    c.execute(CREATE_USER_TABLE)
    c.execute(CREATE_RESERVATION_TABLE)
    db.commit()


def drop_database_tables():
    c.execute(DROP_MOVIE_TABLE)
    c.execute(DROP_PROJECTION_TABLE)
    c.execute(DROP_USER_TABLE)
    c.execute(DROP_RESERVATION_TABLE)
    db.commit()


def insert_movies():
    movies = [("Max Steel", 4.7),
              ("The light Between Oceans", 2.0),
              ("The man who knew", 5.6),
              ("Strorks", 4.3),
              ("Shooter", 2.1),
              ("The man in the high castel", 2.2),
              ("Cossacks", 5.0)]

    c.executemany(INSERT_INTO_MOVIE, movies)
    db.commit()


def insert_projections():
    projec = [(1, '3D', '2016-04-02', '19:00'),
              (3, '2D', '2016-04-05', '19:30'),
              (2, '2D', '2016-04-10', '19:30'),
              (4, '3D', '2016-04-10', '20:00'),
              (3, '3D', '2016-04-12', '20:20'),
              (1, '4DX', '2016-04-13', '20:30'),
              (6, '3D', '2016-04-20', '21:00'),
              (6, '2D', '2016-04-20', '22:00')]

    c.executemany(INSERT_INTO_PROJECTION, projec)
    db.commit()


def insert_users():
    users = [('Matia Vasileva', '478965'),
             ('Vasko Kynev', 'sjii7895F'),
             ('Pepi Petrova', '45kl89H'),
             ('Ceco Mavrinov', '47olkjuT'),
             ('MInka Kurtina', 'eybhusu7uei'),
             ('Teodora Vaseva', 'hGtu56bv'),
             ('Elko Elkov', '56rtfdS0')]
    c.executemany(INSERT_INTO_USER, users)
    db.commit()


def insert_reservations():
    reservations = [(3, 1, 2, 1),
                    (3, 1, 3, 5),
                    (3, 1, 7, 8),
                    (2, 3, 1, 1),
                    (2, 3, 1, 2),
                    (5, 5, 2, 3),
                    (6, 5, 2, 4)]
    c.executemany(INSERT_INTO_RESERVATION, reservations)
    db.commit()


def main():
    drop_database_tables()
    create_database()
    insert_movies()
    insert_projections()
    insert_users()
    insert_reservations()


if __name__ == '__main__':
    main()
