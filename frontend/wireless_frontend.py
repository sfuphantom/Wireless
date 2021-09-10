import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
from collections import deque
import random
import dash_bootstrap_components as dbc


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
#server.secret_key = os.environ.get('secret_key', 'secret')

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app', server=server)

#mqtt = MqttHandler(FRONTEND_NAME, MQTT_BROKER_IP)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

#initial figure of live updating test graph
X = deque(maxlen=10)
X.append(1)
Y = deque(maxlen=10)
Y.append(1)
initial_trace = go.Scatter(x=list(X), y=list(Y), name='Scatter', mode='lines+markers')

app.layout = html.Div(style={'backgroundColor': '#3A3A3A', 'color': '#3A3A3A', 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'},
#style={'backgroundColor': '#3A3A3A'}, 
children = [
  html.H1(children="Wireless GUI",style={'text-align':'center', 'color':'#FF6361'}),
  # first row
  html.Div(dbc.Row(
    [
        # first column of first row
    html.Div(children=[
      dcc.Graph(
        id='live-graph', 
        animate=True, 
        figure={'data': [initial_trace],
        'layout': go.Layout(
          xaxis=dict(range=[min(X), max(X)]), 
          yaxis=dict(range=[min(Y), max(Y)])),
          }
      ),
      dcc.Interval(id='graph-update', interval=1*1000)
    ], style={'display': 'inline-block', 'width': '32%', 'vertical-align': 'top',
    'borderRadius': '15px', 'overflow': 'hidden', 'margin-left': '10px'}),

        # second column of first row
    html.Div(children=[
      dcc.Graph(
        id = 'graph2',
        figure={'data':[go.Scatter(x=[1,3,5,7,8], y=[2,4,6,9,13], line_color='#ffa600')],
        'layout' : go.Layout(title = 'Graph 2',
        paper_bgcolor= '#262626',
        plot_bgcolor = '#262626',
        xaxis=dict(gridcolor = 'white', title = 'x'), 
        yaxis=dict(gridcolor = 'white', title = 'y'),
        font_color = '#FF6361'
        )}
      )
    ], style={'display': 'inline-block', 'width': '32%', 'vertical-align': 'top', 
    'border': '5px grey', 'borderRadius': '15px', 'overflow': 'hidden', 'margin-left': '10px'}),

        # third column of first row
    html.Div(children=[
      dcc.Graph(
        id = 'graph3', 
        figure={'data':[go.Scatter(x=[1,3,7,9,11], y=[3,5,12,14,15], line_color='#ffa600')],
        'layout' : go.Layout(title = 'Graph 3',paper_bgcolor= '#262626',
        plot_bgcolor = '#262626',
        xaxis=dict(gridcolor = 'white', title = 'x'), 
        yaxis=dict(gridcolor = 'white', title = 'y'),
        font_color = '#FF6361')}
      )

    ], style={'display': 'inline-block', 'width': '32%', 'vertical-align': 'top', 
    'borderRadius': '15px', 'overflow': 'hidden', 'margin-left': '10px'}),

  ], no_gutters=True)),

  # second row
  html.Div(
    html.Div(children=[html.Img(src='/assets/stop_button.png',  
      style={'height':'20%', 'width':'20%'}, id='stop-button'),
      html.Div(id='out', children='Press button to stop vehicle', style={'color': 'orange'})],
      style = {'textAlign':'center'}))
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

@app.callback(
  Output(component_id='live-graph', component_property='figure'),
[Input(component_id='graph-update', component_property='n_intervals')])
def update_graph(n):
  X.append(X[-1]+1)
  Y.append(random.randint(0,100))
  #Y.append(mqtt.imu_reading)

  trace = go.Scatter(
    x=list(X),
    y=list(Y),
    name = 'Scatter',
    mode = 'lines+markers', line_color='#ffa600')

  return {'data': [trace], 
  'layout' : go.Layout(
    paper_bgcolor= '#262626',
    plot_bgcolor = '#262626',
    title = 'Battery SoC',
    xaxis=dict(gridcolor = 'white', title = 'time (s)', range=[min(X),max(X)]), 
    yaxis=dict(gridcolor = 'white', title = 'SoC (%)', range=[min(Y),max(Y)]),
    font_color = '#FF6361'
    )}

if __name__ == '__main__':
    app.run_server()
