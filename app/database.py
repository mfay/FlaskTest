# coding: utf-8
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, unique=True)
    firstName = Column(String(255))
    lastName = Column(String(255))
    email = Column(String(255))
