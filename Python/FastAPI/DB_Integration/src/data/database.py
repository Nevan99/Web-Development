from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    show = Column(String, nullable=True)
    user = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    