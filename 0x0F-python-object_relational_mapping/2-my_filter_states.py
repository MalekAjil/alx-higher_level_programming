#!/usr/bin/python3
'''a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
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
    cur.execute("SELECT * FROM states \
                WHERE name = '{}' COLLATE utf8mb4_bin \
                ORDER BY id".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
