from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///imdb.db", echo=False)
base = declarative_base()
Session = sessionmaker(bind=engine)

class movies(base):
    __tablename__ = 'movies'

    movie_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    year = Column(String,nullable=False)
    rating = Column(Float,nullable=False)

class series(base):
    __tablename__ = 'series'

    series_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    year = Column(String,nullable=False)
    seasons = Column(Integer,nullable=False)
    episodes = Column(Integer,nullable=False)

base.metadata.create_all(engine)