from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

# Association table between questions and regions
question_region_association = Table(
    'question_region',
    Base.metadata,
    Column('question_id', Integer, ForeignKey('questions.id')),
    Column('region_id', Integer, ForeignKey('regions.id'))
)

class Region(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    questions = relationship(
        "Question",
        secondary=question_region_association,
        back_populates="regions"
    )
    cycle_config = relationship("CycleConfig", back_populates="region", uselist=False)

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    position_in_cycle = Column(Integer)

    regions = relationship(
        "Region",
        secondary=question_region_association,
        back_populates="questions"
    )

class CycleConfig(Base):
    __tablename__ = 'cycle_configs'
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey('regions.id'), unique=True)
    start_time = Column(DateTime(timezone=True))
    duration = Column(Integer)  # Duration in days

    region = relationship("Region", back_populates="cycle_config")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    region_id = Column(Integer, ForeignKey('regions.id'))

    region = relationship("Region")
