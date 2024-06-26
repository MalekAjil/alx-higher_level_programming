#!/usr/bin/python3
''' a script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
    '''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states
                WHERE name LIKE 'N%' COLLATE utf8mb4_bin ORDER BY id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
