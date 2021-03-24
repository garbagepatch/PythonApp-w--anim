from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
connection = create_engine('sqlite:///LabelBase.db?check_same_thread=False', echo=True)
Session = sessionmaker(bind=connection)


Base = declarative_base()