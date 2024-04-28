#!/usr/bin/python3
'''  script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
    '''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(f"""SELECT cities.name
                FROM cities
                WHERE cities.state_id = (SELECT states.id FROM states
                WHERE states.name = %s)
                ORDER BY cities.id ASC;""",(state_name,))
    rows = cur.fetchall()
    cities = []
    for name in rows:
        cities.append(name[0])
    print(', '.join(cities))
    cur.close()
    db.close()
