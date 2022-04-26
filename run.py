from flask import Flask, request
from src.utils.scraper import scraper
app = Flask(__name__)

@app.route("/")
def index():
    notaUrl = request.args.get("url")
    jsonNota = scraper(notaUrl)
    return jsonNota

app.run()
