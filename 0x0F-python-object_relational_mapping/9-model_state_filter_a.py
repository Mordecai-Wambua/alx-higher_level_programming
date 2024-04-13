#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database."""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a')).order_by(
            State.id)
    for i in states:
        print('{}: {}'.format(i.id, i.name))
    session.close()
