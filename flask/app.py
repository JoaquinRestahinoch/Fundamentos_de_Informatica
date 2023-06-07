from flask import Flask, render_template #Convención de Flask ==> Importar la libreria así y ponerle app.py a la aplicación.
from markupsafe import escape #Cuota de seguridad, verifica que un {id} sea un string y no un JS


prendas = [
    {"id":1,"tipo":"pantalon","talle":42},
    {"id":2,"tipo":"pantalon","talle":56}
]

app = Flask(__name__) #app es el nombre que yo le voy a estar dando a mi servidor

@app.get("/") #Cuando alguien le pegue al / vas a desencadenar la acción de abajo
def home():
    return render_template("home.html") #<p> es la etiqueta de párrafo

@app.get("/prendas")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)} </p>"

