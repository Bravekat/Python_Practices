from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return '{}, {}, {}'.format(self.id, self.task, self.deadline)

    def __str__(self):
        return 'task = {}, deadline = {}'.format(self.task, self.deadline)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
