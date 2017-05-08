from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("encuesta.html")
    
    print request.form

    for key in request.form:
        print key, request.form[key]

    # Guardar las respuestas en un xlsx
    # Procesar las respuestas

    return render_template("encuesta.html")

app.run(host="192.168.0.73", port="4000")