from flask import Flask, request
from src.utils.scraper import scraper
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    notaUrl = request.args.get("url") if(request.args.get("url")) else ""
    jsonNota = scraper(notaUrl)
    return jsonNota

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT"))
