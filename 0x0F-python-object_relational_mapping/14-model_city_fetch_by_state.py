#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State, City.id, City).filter(
            City.state_id == State.id).order_by(City.id).all():
        print('{}: ({}) {}'.format(i.State.name, i.id, i.City.name))

    session.close()
