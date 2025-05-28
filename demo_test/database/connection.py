from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import psycopg2
engine = create_engine('postgresql+psycopg2://postgres:14052005@localhost:5432/demoexam')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()