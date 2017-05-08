from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import json

app = Flask(__name__)

resultados_p1 = {
    "PRI": 0,
    "PAN": 0,
    "PRD": 0,
    "MORENA": 0
}

@app.route("/imagen")
def imagen():
    votos = []

    for partido in resultados_p1:
        num_votos = resultados_p1[partido]
        for i in range(0, num_votos):
            votos.append({
                "Partido": partido
            })

    print votos

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    import StringIO

    fig = Figure()

    ax = fig.add_subplot(111)
    
    import geg

    geg.plot_pie(ax, votos, "Partido")
    
    canvas=FigureCanvas(fig)
    
    png_output = StringIO.StringIO()
    
    canvas.print_png(png_output)
    
    response=make_response(png_output.getvalue())
    
    response.headers['Content-Type'] = 'image/png'
    
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("encuesta.html", partidos = resultados_p1)
    
    r1 = request.form["p1"]; # PRI / PAN / PRD / MORENA

    resultados_p1[r1] += 1;

    return render_template("encuesta.html", partidos = resultados_p1)

app.run(host="localhost", port="4000")