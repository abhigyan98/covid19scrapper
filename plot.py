import random
#from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def create_figure(mainList,states,confirmed):
    fig = Figure()
    ##matplotlib.pyplot.xticks(rotation=90)
    axis = fig.add_subplot(1, 1, 1)
    xs = []
    #xs = range(states)
    for i in range(1,(len(mainList)-1)):
        xs.append(mainList[i][1])
    #ys = [ for x in xs]
    ys = []
    for i in range(states):
        ys.append(int(confirmed[i]))
    axis.bar( xs, ys, color='red')
    axis.plot( xs, ys, color='blue')
    #axis.xticks(rotation=90)
    axis.set_xticklabels(xs,rotation=90,fontsize=5)
    #axis.set_yticklabels(ys, frequency=800)
    return fig
