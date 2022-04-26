from flask import Flask, request
from utils.scraper import scraper
app = Flask(__name__)

@app.route("/")
def index():
    jsonNota = scraper()
    return jsonNota
