import helper
from database import create_connection
from flask import Flask, request, jsonify

app = Flask(__name__)
conn = create_connection("cf.db")
db = conn.cursor()

@app.route('/')
def index():
    return 'hello_world'

# request:
# contestid , index
@app.route('/lookup', methods=["GET", "POST"])
def lookup():
    # lookup on database
    if request.method == 'POST':
        if not request.form['contestid']:
            return None
        if not request.form['index']:
            return None
        look_id = helper.gen_id(request.form['contestid'], request.form['index'])



