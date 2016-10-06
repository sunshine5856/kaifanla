from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

BaseModel = declarative_base()


def init_db ():
    BaseModel.metadata.create_all(db)


def drop_db ():
    BaseModel.metadata.drop_all(db)


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(CHAR(30))
    password = Column(CHAR(30))


if __name__ == "__main__":
    init_db()
    drop_db()
