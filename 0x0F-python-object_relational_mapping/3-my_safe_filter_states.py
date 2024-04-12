#!/usr/bin/python3

"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument safe from MySQL injections.
"""


import MySQLdb
from sys import argv
if __name__ == '__main__':
    connection = MySQLdb.connect(
            host = "localhost",
            user = argv[1],
            password = argv[2],
            database = argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id",(argv[4],))

    output = cursor.fetchall()

    for i in output:
        print(i)
