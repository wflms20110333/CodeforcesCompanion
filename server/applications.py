import json
from helper import suggest_problem, gen_id
from database import create_connection, search, insert_entry, update_entry
from flask import Flask, request, jsonify
import cf_api

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/look')
def lookup():
    if request.args['contestid'] is None:
        return jsonify({})
    if request.args['index'] is None:
        return jsonify({})
    return search(request.args['contestid'], request.args['index'], gen_id(request.args['contestid'], request.args['index']))

@app.route('/insert')
def insert():
    if request.args['contestid'] and request.args['index'] and request.args['rating'] and request.args['tags']:
        look_id = gen_id(request.args['contestid'], request.args['index'])
        insert_entry(look_id, request.args['rating'], request.args['tags'])
    return 'done'

@app.route("/checkHandle")
def checkHandle():
    return jsonify({'valid': cf_api.isValidUser(request.args['handle']), 'handle': request.args['handle']})

@app.route('/update')
def update():
    if request.args['contestid'] and request.args['index'] and request.args['rating'] and request.args['tags']:
        look_id = gen_id(request.args['contestid'], request.args['index'])
        update_entry(look_id, request.args['rating'], request.args['tags'])
    return 'done'

@app.route('/suggest')
def suggest():
    if request.args['handle'] and request.args['tag']:
        number, letter = suggest_problem(request.args['tag'], request.args['handle'])
        return jsonify({
            'number' : number,
            'letter' : letter
        });
    return jsonify({})