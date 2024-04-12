#!/usr/bin/python3

"""Lists all cities from the database hbtn_0e_4_usa."""


import MySQLdb
from sys import argv
if __name__ == '__main__':
    connection = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT b.id, b.name, a.name\
            FROM cities AS b\
            INNER JOIN states AS a\
            ON b.state_id = a.id\
            ORDER BY b.id;")

    output = cursor.fetchall()

    for i in output:
        print(i)
