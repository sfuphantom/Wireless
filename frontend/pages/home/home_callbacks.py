import dash
from dash.dependencies import Input, Output
import dash_daq

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
@app.callback([Output(component_id='live-graph-1', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
              #[Input('radio_items', 'n_intervals')])
def update_data(n):
  returned_data = []
  try:
    for graph in graphs_list:
      if graph['title'] in ("Battery SOC"):
        graph['X'] += 1
        #graph['Y'] = mqtt.data_dict[graph["data_key"]]
        graph['Y'] = (random.randint(0,100))
        returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 15])

# tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data
  except Exception as e:
    print(e)

# @app.callback([Output(component_id='live-graph-3', component_property='extendData')],
#               [Input('graph-interval-2', 'n_intervals')])
# def update_gps(n):
#   returned_data = []
#   try:
#     graph = graphs_list[2]
#     graph['X'] += 1
#     #graph['Y'] = mqtt.data_dict[graph["data_key"]]
#     graph['Y'] = (random.randint(0,100))
#     returned_data = [[dict(x=[[graph['X']],[graph['X']],[graph['X']],[graph['X']]],\
#                     y=[[graph['Y']],[random.randint(0,100)],[random.randint(0,100)],[random.randint(0,100)]]), [0,1,2,3], 15]]

# tuple is (dict of new data, target trace index, number of points to keep)
  #   return returned_data
  # except Exception as e:
  #   print(e)  

@app.callback([Output(component_id='XYZ-Linear-Acceleration', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
def update_xyz_linear_acc(n):
  returned_data = []
  try:
    graph = graphs_list[3]
    graph['X'] += 1
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    graph['Y'] = (random.randint(0,100))
    returned_data = [[dict(x=[[graph['X']],[graph['X']],[graph['X']], [graph['X']]],\
                    y=[[graph['Y']],[random.randint(0,100)], [random.randint(0,100)],[random.randint(0,100)]]), [0,1,2,3], 10]]

# tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='live-graph-2', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
def update_pedal_angle(n):
  returned_data = []
  try:
    graph = graphs_list[1]
    graph['X'] += 1
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    Y = random.randint(0,100)
    graph['Y'] = Y
    returned_data = [[dict(x=[[graph['X']], [graph['X']], [graph['X']]],\
                    y=[[graph['Y']], [1-Y], [random.randint(0,100)]]), [0,1,2], 10]]

# tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='live-graph-5', component_property='extendData')],
              [Input('graph-interval-1', 'n_intervals')])
def update_xyz_linear_acc(n):
  returned_data = []
  try:
    graph = graphs_list[4]
    graph['X'] += 1
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    graph['Y'] = (random.randint(0,100))
    returned_data = [[dict(x=[[graph['X']],[graph['X']],[graph['X']], [graph['X']]],\
                    y=[[graph['Y']],[random.randint(0,100)], [random.randint(0,100)],[random.randint(0,100)]]), [0,1,2,3], 10]]

# tuple is (dict of new data, target trace index, number of points to keep)
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='gauge', component_property='value')],
              [Input('graph-interval-1', 'n_intervals')])
              #[Input('radio_items', 'n_intervals')])
def update_gauge(n):
    value_out = random.randint(0,100)
    return [value_out]