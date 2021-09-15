import dash
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objs as go
from app import app, mqtt
from utils.constants import graphs_list

import random
import numpy as np

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

# Graph update
@app.callback([Output(component_id='live-graph-1', component_property='extendData'),
               Output(component_id='live-graph-2', component_property='extendData'),
               Output(component_id='live-graph-3', component_property='extendData'),
               Output(component_id='live-graph-4', component_property='extendData'),
               Output(component_id='live-graph-5', component_property='extendData'),
               Output(component_id='live-graph-6', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
def update_data(n_intervals):
    returned_data = []

    for graph in graphs_list:
      graph['X'] += 1
      graph['Y'] = mqtt.data_dict[graph["data_key"]]

      returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 10])

    # tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data