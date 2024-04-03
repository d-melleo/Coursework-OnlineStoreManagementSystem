from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from PyQt5.QtSql import QSqlDatabase
path = 'sqlite:///mydatabase.db'
engine = create_engine(path)
dbQ = QSqlDatabase.addDatabase("QSQLITE")
dbQ.setDatabaseName('mydatabase.db')
Base.metadata.create_all(engine)
# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()
