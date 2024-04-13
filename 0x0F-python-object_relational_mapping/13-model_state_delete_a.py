#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a."""

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

    change = session.query(State).filter(State.name.contains('a'))
    if change:
        for i in change:
            session.delete(i)

    session.commit()

    session.close()
