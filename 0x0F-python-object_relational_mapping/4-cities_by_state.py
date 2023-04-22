#!/usr/bin/python3
'''Mysql'''
import MySQLdb
from sys import argv


if __name__=='__main__':
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3],
            charset="utf8"
    )
    db = connection.cursor()
    db.execute("SELECT cities.id, cities.name, states.name FROM CITIES" +
               " INNER JOIN states ON cities.state_id = states.id" +
               " ORDER BY cities.id ASC;"
    query_rows = db.fetchall()

    for row in query_rows:
        print(row)

    db.close()
    conn.close()

