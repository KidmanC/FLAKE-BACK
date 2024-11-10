from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'USER'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)