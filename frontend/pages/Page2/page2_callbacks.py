import dash
from dash.dependencies import Input, Output
import dash_daq

import plotly.express as px
import plotly.graph_objs as go
from app import app, mqtt
from utils.constants import graphs_list

import random
import numpy as np

@app.callback([Output(component_id='battery-temp-graph', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
def update_data(n):
  returned_data = []
  try:
    for graph in graphs_list:
      if graph['title'] == "Battery Temperature":
        graph['X'] += 1
        #graph['Y'] = mqtt.data_dict[graph["data_key"]]
        graph['Y'] = (random.randint(0,100))
        returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 15])

# tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data
  except Exception as e:
    print(e)