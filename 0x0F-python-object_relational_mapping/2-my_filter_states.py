#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""


import MySQLdb
from sys import argv
if __name__ == '__main__':
    connection = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id".format(argv[4]))

    output = cursor.fetchall()

    for i in output:
        print(i)
