from flask import Flask, render_template, request,redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")
