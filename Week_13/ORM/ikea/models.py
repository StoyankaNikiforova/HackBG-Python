import sqlite3
from base import FieldsMeta
from settings import DB_NAME


class BaseModel(metaclass=FieldsMeta):
    __tablename__ = None
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    c = connection.cursor()

    @classmethod
    def create_all_tables(cls):
        pass
