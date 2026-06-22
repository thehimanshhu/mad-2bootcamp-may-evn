from app import app
from flask import request
@app.route("/")
def home():
    return "Hello"

