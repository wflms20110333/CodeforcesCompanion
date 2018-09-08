import sqlite3
from sqlite3 import Error

create_problem_table = "CREATE TABLE IF NOT EXISTS problems ("\
    "id INTEGER PRIMARY KEY,"\
    "rating INTEGER,"\
    "tags BLOB"\
");"

def create_connection(filename):
    try:
        conn = sqlite3.connect(filename)
        if conn is not None:
            create_table(conn.cursor(), create_problem_table)
    except Error as e:
        print(e)
    return conn

def create_table(cursor, sql_command):
    try:
        cursor.execute(sql_command)
    except Error as e:
        print(e)