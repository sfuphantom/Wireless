import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
from collections import deque
import random

import flask
import pandas as pd
import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mqtt_handler import *

FRONTEND_NAME = "Frontend"
MQTT_BROKER_IP = "localhost"

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app', server=server)

mqtt = MqttHandler(FRONTEND_NAME, MQTT_BROKER_IP)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'



# test_graph = GraphComponent({'x':[1,3,5,2,7,8], 'y':[2,4,6,9,3,0]}, "Test",
#                            "test-class", "graph-1", "container-1")
# test_graph.style = {'width': '40%', 'height': '20%'}

# app.layout = html.Div([
#   test_graph
# ], className="container", style={"background-image": "linear-gradient(180deg, blue, lightblue)"})
df = pd.DataFrame ({'x':[1,3,5,2,7,8], 'y':[2,4,6,9,3,0]})
fig = go.Figure(data=[go.Scatter(x=[1,3,5,2,7,8], y=[2,4,6,9,3,0])], 
layout_title_text='Battery SOC')

#initial figure of live updating test graph
X = deque(maxlen=10)
X.append(1)
Y = deque(maxlen=10)
Y.append(1)
initial_trace = go.Scatter(x=list(X), y=list(Y), name='Scatter', mode='lines+markers')



app.layout = html.Div(children = [
  #stop button 
  html.Img(src=app.get_asset_url('stop_button.png'),  #(src='assets/stop_button.png', 
    style={'height':'20%', 'width':'20%'}, id='stop-button'),
    html.Div(id='out', children='Press button to stop vehicle'),
  
  #test graph
  dcc.Graph(
     id='test-graph',
     figure= fig
     ),
  
  #test graph with live updating
  dcc.Graph(
    id='live-graph', 
    animate=True, 
    figure={'data': [initial_trace],
    'layout': go.Layout(
      title = 'Battery SoC',
      xaxis=dict(range=[min(X), max(X)]), 
      yaxis=dict(range=[min(Y), max(Y)]))
      }),
  dcc.Interval(id='graph-update', interval=1*1000),
])

#button click
@app.callback(
  Output(component_id='out', component_property='children'),
  Input(component_id='stop-button', component_property= 'n_clicks') 
)
def button_clicked(n_clicks):
  if n_clicks is None:
    return dash.no_update

  mqtt.client.publish(MQTT_PUB_TOPICS['SHUTDOWN_TOPIC'],
                    payload=1,
                    qos=2,
                    retain=False)
  return 'stop button pressed'

@app.callback(Output('live-graph', 'figure'),
[Input('graph-update', 'n_intervals')])
def update_graph(n):
  X.append(X[-1]+1)
  #Y.append(Y[-1]+2)
  Y.append(mqtt.imu_reading)

  trace = go.Scatter(
    x=list(X),
    y=list(Y),
    name = 'Scatter',
    mode = 'lines+markers')

  return {'data': [trace], 
  'layout' : go.Layout(
    xaxis=dict(title = 'time (s)', range=[min(X),max(X)]), 
    yaxis=dict(title = 'SoC (%)', range=[min(Y),max(Y)]))}

if __name__ == '__main__':
    app.run_server()