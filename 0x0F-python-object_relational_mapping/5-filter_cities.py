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
    cursor.execute("SELECT b.name\
            FROM cities AS b\
            LEFT JOIN states AS a\
            ON a.id = b.state_id\
            WHERE a.name = '{}'\
            ORDER BY b.id;".format(argv[4]))

    output = cursor.fetchall()

    print(", ".join([i[0] for i in output]))
