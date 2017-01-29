from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine

Base = declarative_base()


class BaseUser(Base):
    __tablename__ = 'user'
    id = Colimn(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    passowrd = Column(String(250), nullable=False)


class Course(BaseUser):
    __tablename__ = 'course'
    id = Colimn(Integer, ForeignKey('iser.id'), primary_key=True)
    mac = Column(String(30), nullable=False)
    course = Column(String(250), ForeignKey('course.id'))


class Student(BaseUser):
    __tablename__ = 'student'
    id = Colimn(Integer, ForeignKey('iser.id'), primary_key=True)
    mac = Column(String(30), nullable=False)
    course = Column(String(250), ForeignKey('course.id'))


DB_NAME = 'Odin.db'

engine = create_engin(DB_NAME)
Base.metadata.create_all(engine)
