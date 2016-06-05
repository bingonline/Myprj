
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData

import socket
import struct

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    password = Column(String(20))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

# # Base.metadata.create_all(engine)


def testDB():
    engine = create_engine('mysql://root:zkd@localhost:3306/test', convert_unicode=True,echo=True)
    Base.metadata.create_all(engine)


if __name__=='__main__':
    testDB()