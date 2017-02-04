from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from settings import DB_NAME

Base = declarative_base()


class Mentor(Base):
    __tablename__ = 'mentor'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Integer, nullable=False)
    picture = Column(String, nullable=False)
    teams = Column(Integer, ForeignKey("team.id"))
    team = relationship("team", backref="teams")


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    idea_description = Column(String, nullable=False)
    repository = Column(String, nullable=False)
    technologies_full = Column(Integer, ForeignKey('skills.id'))
    skills = relationship("skills", backref="team")
    need_more_members = Column(Boolean, unique=False, default=True)
    members_needed_desc = Column(String, nullable=False)
    room = Column(Integer, nullable=False)
    place = Column(String, default=None)
    mentor = Column(Integer, nullable=False)


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    publicteam = relationship()

    def __str__(cls):
        return cls.name


engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
