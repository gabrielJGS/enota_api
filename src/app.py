import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})
