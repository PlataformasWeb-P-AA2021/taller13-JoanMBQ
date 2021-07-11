from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola Mundo</p>"


@app.route("/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=('JoanMBQ', '12345678'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)

@app.route("/departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('JoanMBQ', '12345678'))
    datos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_propietario':d['nombre_propietario'],'costo':d['costo'] ,
        'num_cuartos':d['num_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero_departamentos=numero_departamentos)


def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('JoanMBQ', '12345678'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
