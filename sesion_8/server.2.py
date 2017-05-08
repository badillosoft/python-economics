from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

resultados_p1 = {
    "PRI": 0,
    "PAN": 0,
    "PRD": 0,
    "MORENA": 0
};

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("encuesta.html", partidos = resultados_p1)
    
    r1 = request.form["p1"];

    resultados_p1[r1] += 1;

    return render_template("encuesta.html", partidos = resultados_p1)

app.run(host="192.168.0.73", port="4000")