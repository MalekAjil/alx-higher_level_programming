#!/usr/bin/python3
''' a script lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities, states
                WHERE cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
