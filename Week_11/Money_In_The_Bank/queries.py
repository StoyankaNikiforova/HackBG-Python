DROP_CLIENT_TABLE = '''
    DROP TABLE IF EXISTS CLIENT
'''


CREATE_CLIENT_TABLE = '''CREATE TABLE IF NOT EXISTS CLIENT(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USERNAME TEXT,
                        PASSWORD TEXT,
                        BALANCE REAL DEFAULT 0,
                        MESSAGE TEXT)'''


SET_CLIENT_MESSAGE = '''UPDATE CLIENT
                           SET MESSAGE = ? WHERE ID = ?
                        '''

SET_CLIENT_PASSWORD = '''UPDATE CLIENT
                           SET PASSWORD = ? WHERE ID = ?
                        '''


INSERT_INTO_CLIENT = '''INSERT INTO CLIENT(USERNAME, PASSWORD)
                        VALUES(?, ?)
                        '''


GET_CLIENT_FROM_DB = '''SELECT *
                        FROM CLIENT
                        WHERE USERNAME = ? AND PASSWORD = ?
                        LIMIT 1'''
