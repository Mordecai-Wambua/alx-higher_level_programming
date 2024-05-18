#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Class state definition inheriting from Base."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state")
