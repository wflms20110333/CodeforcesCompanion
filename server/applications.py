import helper
from database import create_connection
from flask import Flask, request, jsonify
from flask_session import Session
from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)
conn = create_connection("cf.db")
db = conn.cursor()

@app.route('/')
def index():
    return 'hello'

@app.route('/look')
def lookup():
    if request.args['contestid'] is None:
        return 'hi'
    if request.args['index'] is None:
        return 'hello'
    look_id = helper.gen_id(request.args['contestid'], request.args['index'])
    res = db.execute("SELECT * FROM problems WHERE id = {0}".format(look_id)).fetchall()
    if not res:
        return 'ur bad'
    return jsonify({
        'contestID' : request.args['contestid'],
        'index' : request.args['index'],
        'name' : res[0][1],
        'rating' : res[0][2],
        'tags' : res[0][3]
    })


@app.route('/insert')
def insert():
    # test for possible defects
    look_id = helper.gen_id(request.args['contestid'], request.args['index'])
    res = db.execute("INSERT INTO problems (id, name, )")