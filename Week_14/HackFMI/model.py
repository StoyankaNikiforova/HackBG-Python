from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Table
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from settings import DB_NAME

Base = declarative_base()


mentor_team = Table('mentors_teams', Base.metadata,
                    Column('mentot_id', Integer, ForeignKey('mentor.id')),
                    Column('team_id', Integer, ForeignKey('team.id')))

team_skills = Table('teams_skills', Base.metadata,
                    Column('team_id', Integer, ForeignKey('team.id')),
                    Column('skill_id', Integer, ForeignKey('skills.id')))


class Mentor(Base):
    __tablename__ = 'mentor'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Integer, nullable=False)
    picture = Column(String, nullable=False)
    teams = relationship("Team",
                         secondary=mentor_team,
                         backref="mentors")


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    idea_description = Column(String, nullable=False)
    repository = Column(String, nullable=False)
    technologies_full = relationship("Skills",
                                     secondary=team_skills,
                                     backref="teams")

    need_more_members = Column(Boolean, unique=False, default=True)
    members_needed_desc = Column(String, nullable=False)
    room = Column(Integer, nullable=False)
    place = Column(String, default=None)


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __str__(cls):
        return cls.name


engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
