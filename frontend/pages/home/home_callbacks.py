import dash
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objs as go
from app import app, mqtt

from collections import deque
import random
import numpy as np

#initial figure of live updating test graph
X = deque(maxlen=10)
X.append(1)
Y = deque(maxlen=10)
Y.append(1)
initial_trace = go.Scatter(x=list(X), y=list(Y), name='Scatter', mode='lines+markers')

resolution = 10
t = np.linspace(0, np.pi * 2, resolution)
x, y = np.cos(t), np.sin(t)

graphs_list = [
  {
    "title": "Acceleration on X-axis",
    "X": deque(maxlen=10),
    "Y": deque(maxlen=10),
    "data_key": "ax"
  },
  {
    "title": "Acceleration on Y-axis",
    "X": deque(maxlen=10),
    "Y": deque(maxlen=10),
    "data_key": "ay"
  },
  {
    "title": "Acceleration on Z-axis",
    "X": deque(maxlen=10),
    "Y": deque(maxlen=10),
    "data_key": "az"
  }
] 

for graph in graphs_list:
  graph['X'].append(1)
  graph['Y'].append(1)

#button click
@app.callback(
  Output(component_id='out', component_property='children'),
  Input(component_id='stop-button', component_property= 'n_clicks') 
)
def button_clicked(n_clicks):
  try:
    if n_clicks is None:
      return dash.no_update

    mqtt.triggerShutdown(1)
    return 'stop button pressed'
  except Exception as e:
    print(e)


@app.callback(
  [Output(component_id='live-graph-1', component_property='figure'),
   Output(component_id='live-graph-2', component_property='figure'),
   Output(component_id='live-graph-3', component_property='figure')],
  [Input(component_id='graph-interval-1', component_property='n_intervals')]
)
def update_graph(n):
  try:
    #X.append(X[-1]+1)
    #Y.append(random.randint(0,100))
    #Y.append(mqtt.imu_reading_x)
    returned_graphs = []
    for graph in graphs_list:
      graph['X'].append(graph['X'][-1]+1)
      graph['Y'].append(mqtt.data_dict[graph["data_key"]])

      fig = go.Figure()
      fig.add_traces(
        go.Scatter(
          x=list(graph['X']),
          y=list(graph['Y']),
          name = 'Scatter',
          mode = 'lines+markers', line_color='#ffa600')
      )

      fig.update_layout(
        uirevision='constant',
        paper_bgcolor= '#262626',
        plot_bgcolor = '#262626',
        title = graph['title'],
        xaxis=dict(gridcolor = 'white', title = 'time (s)', range=[min(graph['X']),max(graph['X'])]), 
        yaxis=dict(gridcolor = 'white', title = 'Acc (m/s2)', range=[min(graph['Y']),max(graph['Y'])]),
        font_color = '#FF6361'
      )

      returned_graphs.append(fig)

    graph = graphs_list[0]
    print("hello")

    return [dict(x=[graph['X'][-1]], y=[mqtt.data_dict[graph["data_key"]]]), [0], 10],\
           [dict(x=[graph['X'][-1]], y=[mqtt.data_dict[graph["data_key"]]]), [0], 10],\
           [dict(x=[graph['X'][-1]], y=[mqtt.data_dict[graph["data_key"]]]), [0], 10]

  except Exception as e:
    print(e)