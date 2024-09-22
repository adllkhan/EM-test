from sqlalchemy import Column, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
