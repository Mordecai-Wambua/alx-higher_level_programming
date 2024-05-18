#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”."""

from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    s1 = State(name='California')
    c1 = City(name='San Francisco')
    s1.cities.append(c1)

    session.add(s1)
    session.add(c1)
    session.commit()

    session.close()
