from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine
from settings import DB_NAME

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(1100), nullable=False)
    balance = Column(String(250), nullable=False, default=0)
    message = Column(String(250), nullable=False, default='Hello!')


engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
