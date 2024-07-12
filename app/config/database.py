import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Connection to DataBase
engine = create_engine(DATABASE_URL)
# Make Session to DataBase
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Instance to make models
Base = declarative_base()

# Function to obtain database session
def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()