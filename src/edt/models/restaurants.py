from sqlalchemy import CheckConstraint, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurants(Base):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True)
    rating = Column(Integer, CheckConstraint("rating >= 0 AND rating <= 4"))
    name = Column(String)
    site = Column(String)
    email = Column(String)
    phone = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    lat = Column(Float)
    lng = Column(Float)
