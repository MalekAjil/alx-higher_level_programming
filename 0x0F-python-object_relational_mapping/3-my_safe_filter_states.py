#!/usr/bin/python3
''' a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states\
                WHERE name LIKE %s ORDER BY id ASC;", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
