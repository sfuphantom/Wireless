import dash
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objs as go
from app import app

from collections import deque
import random

#initial figure of live updating test graph
X = deque(maxlen=10)
X.append(1)
Y = deque(maxlen=10)
Y.append(1)
initial_trace = go.Scatter(x=list(X), y=list(Y), name='Scatter', mode='lines+markers')

graphs_list = [
  {
    "title": "Acceleration on X-axis",
  },
  {
    "title": "Acceleration on Y-axis",
  },
  {
    "title": "Acceleration on Z-axis",
  }
] 

#button click
@app.callback(
  Output(component_id='out', component_property='children'),
  Input(component_id='stop-button', component_property= 'n_clicks') 
)
def button_clicked(n_clicks):
  try:
    if n_clicks is None:
      return dash.no_update

    """mqtt.client.publish(MQTT_PUB_TOPICS['SHUTDOWN_TOPIC'],
                      payload=1,
                      qos=2,
                      retain=False)"""
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
    X.append(X[-1]+1)
    Y.append(random.randint(0,100))
    #Y.append(mqtt.imu_reading_x)

    returned_graphs = []
    for graph in graphs_list:
      fig = go.Figure()
      fig.add_traces(
        go.Scatter(
          x=list(X),
          y=list(Y),
          name = 'Scatter',
          mode = 'lines+markers', line_color='#ffa600')
      )

      fig.update_layout(
        uirevision='constant',
        paper_bgcolor= '#262626',
        plot_bgcolor = '#262626',
        title = graph['title'],
        xaxis=dict(gridcolor = 'white', title = 'time (s)', range=[min(X),max(X)]), 
        yaxis=dict(gridcolor = 'white', title = 'Acc (m/s2)', range=[min(Y),max(Y)]),
        font_color = '#FF6361'
      )

      returned_graphs.append(fig)

    return returned_graphs
  except Exception as e:
    print(e)