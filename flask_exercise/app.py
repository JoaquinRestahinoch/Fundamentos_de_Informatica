from flask import Flask, render_template, request,redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/resultados/")
def get_resultados():
    return render_template("resultados.html")

@app.get("/plan_2023/")
def get_conclusiones():
    return render_template("conclusiones.html")