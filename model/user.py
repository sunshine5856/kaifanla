from sqlalchemy import Table, Column, Integer, ForeignKey, CHAR
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

BaseModel = declarative_base()


def init_db():
    BaseModel.metadata.create_all(db)


def drop_db():
    BaseModel.metadata.drop_all(db)


class UserOrm(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))
    password = Column(CHAR(30))


class User(object):
    def __init__(self):
        # try:
        #     eng = creat_engine('sqlite:///memory')
        # except ImportError:
        #     raise RuntimeError()
        # try:
        #     eng.connect()
        # except exc.OpertionError:
        #     eng.creat_engine(dirname(dsn))
        #     eng.ex
        pass


if __name__ == "__main__":
    init_db()
    drop_db()
