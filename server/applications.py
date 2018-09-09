import helper
from database import create_connection, search, insert_entry, update_entry, query_tag
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
    return search(request.args['contestid'], request.args['index'], helper.gen_id(request.args['contestid'], request.args['index']))

@app.route('/insert')
def insert():
    if request.args['contestid'] and request.args['index']:
        look_id = helper.gen_id(request.args['contestid'], request.args['index'])
        insert_entry(look_id, request.args['rating'], request.args['tags'])
    return 'hi'

@app.route("/checkHandle")
def checkHandle():
    return jsonify({'valid': cf_api.isValidUser(request.args['handle']), 'handle': request.args['handle']})

@app.route('/update')
def update():
    if request.args['contestid'] and request.args['index']:
        look_id = helper.gen_id(request.args['contestid'], request.args['index'])
        update_entry(look_id, request.args['rating'], request.args['tags'])
    return 'hi'

@app.route('/looktag')
def looktag():
    if request.args['tag']:
        return query_tag(request.args['tag'])
    return jsonify({})