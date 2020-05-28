import requests
import bs4
from flask import *
import io
import test
import dash
import dash_core_components as dcc
import dash_html_components as html


server=Flask(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheets)


def getHtmlData(url):
    data=requests.get(url)
    return data

@server.route("/")
def coronaDetails():    
    mainList=test.test()
    total=test.siteCount()
    return render_template("index.html", mainList=mainList, total=total)

mainList=test.test()

state=[]  
totalCase=[]
cured=[]
death=[]
for i in range(1,len(mainList)):
    state.append(mainList[i][1])
    totalCase.append(mainList[i][2])
    cured.append(mainList[i][3])
    death.append(mainList[i][4])
    
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)
app.layout = html.Div(children=[
    
        dcc.Graph(
                figure={
                    'data': [
                        {
                            'x': state,
                            'y': totalCase,
                            # 'y': cured,
                            # 'y': death,
                            'type': 'bar',
                            'name': 'Total Confirmed Cases',
                            'marker' : { "color" : '#E74C3C'}
                        },
                        {
                            'x': state,
                            # 'y': totalCase,
                            'y': cured,
                            # 'y': death,
                            'type': 'bar',
                            'name': 'Cured/Migrate/Recovered Cases',
                            'marker' : { "color" : '#28B463'}
                        },
                        {
                            'x': state,
                            # 'y': totalCase,
                            # 'y': cured,
                            'y': death,
                            'type': 'bar',
                            'name': 'Death Cases',
                            'marker' : { "color" : '#34495E'}
                        },
                    ],
                    'layout': dict(
                    height= 1200,
                    padding= 100,
                    # 'width': '148%'
                    margin={'b':200},
                    legend={'x': 1, 'y': 1},
                )
                }),
    ])

if __name__ == "__main__":
    #coronaDetails()
    app.run_server(host='0.0.0.0', port=5002, debug=True)