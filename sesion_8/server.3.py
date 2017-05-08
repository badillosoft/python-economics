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
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
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
    
    r1 = request.form["p1"];

    resultados_p1[r1] += 1;

    return render_template("encuesta.html", partidos = resultados_p1)

app.run(host="localhost", port="4000")