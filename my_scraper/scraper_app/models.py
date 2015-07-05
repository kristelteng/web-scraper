from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime

import settings

DeclarativeBase = declarative_base()


def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	"""
	return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    address = Column('address', String, nullable=True)
    contact = Column('contact', String, nullable=True)
    hours = Column('hours', String, nullable=True)
    website = Column('website', String, nullable=True)
    photo = Column('photo', String, nullable=True)
    desc = Column('desc', String, nullable=True)
    video = Column('video', String, nullable=True)
