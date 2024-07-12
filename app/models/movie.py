from sqlalchemy import Column, MetaData, String, Table, Text, Integer

from app.config.database import Base

class Movie(Base):
    __tablename__ = 'movie'
    id_movie = Column(Integer, primary_key=True, unique=True, nullable=False)
    title    = Column(String(80), nullable=False)