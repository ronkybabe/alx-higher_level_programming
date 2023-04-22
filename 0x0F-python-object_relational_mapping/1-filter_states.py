#!/usr/bin/python3
'''Mysql'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3],
            charset="utf8"
        )
    db = conn.cursor()
    db.execute("SELECT * FROM states WHERE name IS NOT " +
                "NULL AND LEFT(CAST(name AS BINARY), 1) = 'N'ORDER BY id ASC;")
    query_rows = db.fetchall()

    for row in query_rows:
        print(row)

    db.close()
    conn.close()
