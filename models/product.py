from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Product(Base):
    __tablename__ = 'PRODUCT'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    created_by = Column(Integer, ForeignKey('USER.id'))