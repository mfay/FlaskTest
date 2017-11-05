# coding: utf-8
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.ext.declarative import declarative_base
from flaskr.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, unique=True)
    firstName = Column(String(255))
    lastName = Column(String(255))
    email = Column(String(255))

    # def __init__(self, firstName=None, lastName=None, email=None):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.email = email