GET_PASS_BY_USER = '''SELECT PASSWORD
                      FROM USER AS U
                      WHERE USERNAME = ?'''

GET_USER_ID_BY_NAME = '''SELECT ID
                    FROM USER
                    WHERE USERNAME = ?'''


GET_MOVIES = '''SELECT *
                FROM MOVIE
                ORDER BY RATING'''

GET_MOVIES_PROJECTIONS = '''SELECT P.ID, M.NAME, P.DATE, P.TIME
                            FROM MOVIE AS M
                            JOIN PROJECTION AS P
                            WHERE M.ID=?'''

GET_RESERVED_SPOTS = '''SELECT ROW, COL
                        FROM RESERVATION
                        WHERE PROJECTION_ID = ?'''


GET_PROJECTION_INFO = '''SELECT M.NAME, P.DATE, P.TIME
                         FROM MOVIE AS M
                         JOIN PROJECTION AS P
                         WHERE P.ID=?'''
