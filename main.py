import requests
import bs4
from flask import *
#import numpy as np
import plot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import matplotlib.pyplot as plt
import test


app=Flask(__name__)

def getHtmlData(url):
    data=requests.get(url)
    return data

@app.route("/")
def coronaDetails():    
    mainList=test.test()
    total=test.siteCount()
    return render_template("index.html", mainList=mainList, total=total)

@app.route('/plot.png')
def plot_png():
    mainList=test.test()
    confirmed = []
    for i in range(1,len(mainList)-1):
        confirmed.append(mainList[i][2])
    
    fig = plot.create_figure(mainList,(len(mainList)-2),confirmed)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



if __name__ == "__main__":
    #coronaDetails()
    app.run(host='0.0.0.0', port=5000, debug=True)