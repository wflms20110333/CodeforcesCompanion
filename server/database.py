__author__ = "Aditya Arjun, Richard Guo, An Nguyen, Elizabeth Zou"
__copyright__ = "Copyright 2018-present, Codeforces Companion (Coco)"

import sqlite3
import json
from sqlite3 import Error
from flask import jsonify

create_problem_table = "CREATE TABLE IF NOT EXISTS problems ("\
    "id INTEGER PRIMARY KEY,"\
    "problemID INTEGER UNIQUE,"\
    "rating INTEGER,"\
    "tags TEXT"\
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

def insert_entry(problemID, rating, tags):
    try:
        conn = create_connection("cf.db")
        db = conn.cursor()
        db.execute('INSERT INTO problems (problemID, rating, tags) VALUES (?,?,?);', (int(problemID), int(rating), str(tags)))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()

def update_entry(problemID, rating, tags):
    try:
        conn = create_connection("cf.db")
        db = conn.cursor()
        db.execute('UPDATE INTO problems (problemID, rating, tags) VALUES (?,?,?);', (int(problemID), int(rating), str(tags)))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()

def query_tag(tag):
    try:
        conn = create_connection("cf.db")
        db = conn.cursor()
        res = db.execute('SELECT * FROM problems WHERE tags LIKE "%' + str(tag) +'%"').fetchall()
        if not res:
            return []
        conn.close()
        return res
    except Error as e:
        print(e)
    finally:
        conn.close()
    return []

def get_rating(problemID):
    try:
        conn = create_connection("cf.db")
        db = conn.cursor()
        res = db.execute("SELECT * FROM problems WHERE problemID = " + str(problemID)).fetchall()
        if not res:
            return 1500
        conn.close()
        return res[0][2]
    except Error as e:
        print(e)
    finally:
        conn.close()
    return 1500
def search(contestID, index, problemID):
    try:
        conn = create_connection("cf.db")
        db = conn.cursor()
        res = db.execute("SELECT * FROM problems WHERE problemID = " + str(problemID)).fetchall()
        if not res:
            return jsonify({})
        conn.close()
        return jsonify({
            'contestID' : contestID,
            'index' : index,
            'rating' : res[0][2],
            'tags' : res[0][3]
        })
    except Error as e:
        print(e)
    finally:
        conn.close()
    return jsonify({})