#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    connection = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3])

    db_cursor = connection.cursor()
    db_cursor.execute("SELECT * FROM states")

    output = db_cursor.fetchall()

    for i in output:
        print(i)
