import helper
from database import create_connection
from flask import Flask, request, jsonify

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
        'rating' : res[0][1],
        'tags' : res[0][2]
    })


@app.route('/insert')
def insert():
    if not request.args['contestid'] or not request.args['index'] or not request.args['rating'] or not request.args['tags']:
        return None
    look_id = helper.gen_id(request.args['contestid'], request.args['index'])
    res = db.execute("INSERT INTO problems (id, rating, tags) VALUES ({}, {}, {})".format(
        look_id, request.args['rating'], request.args['tags']))

@app.route('/update')
def update():
    if not request.args['contestid'] or not request.args['index'] or not request.args['rating'] or not request.args['tags']:
        return None
    look_id = helper.gen_id(request.args['contestid'], request.args['index'])
    res = db.execute("UPDATE INTO problems (id, rating, tags) VALUES ({}, {}, {})".format(
        look_id, request.args['rating'], request.args['tags']))