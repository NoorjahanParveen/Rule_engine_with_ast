from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from config import Config  # Import the Config class

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule = Column(String, nullable=False)
    ast = Column(JSON, nullable=False)

# Database setup using the URI from config.py
DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI  # Use the database URI from config
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)  # Create tables if they don't exist
db_session = sessionmaker(bind=engine)()  # Create a session instance

