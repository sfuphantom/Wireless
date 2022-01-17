import dash
from dash.dependencies import Input, Output, State
import dash_daq

import plotly.express as px
import plotly.graph_objs as go
from app import app, mqtt
from components.graph_component import GraphComponent
from utils.constants import graphs_list
from datetime import datetime

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

@app.callback(Output(component_id = 'pedalangle_interval', component_property='interval'),
             [Input('pedalangle-rate', 'value')])
def update_interval(val):
  return val*1000 

@app.callback(Output(component_id = 'batterysoc_interval', component_property='interval'),
             [Input('batterySOC-rate', 'value')])
def update_interval(val):
  return val*1000 

@app.callback(Output(component_id = 'XYZgyroscope-interval', component_property='interval'),
             [Input('XYZgyroscope-rate', 'value')])
def update_interval(val):
  return val*1000 

@app.callback(Output(component_id = 'XYZlinear-interval', component_property='interval'),
             [Input('XYZlinear-rate', 'value')])
def update_interval(val):
  return val*1000 



# Graph update
@app.callback([Output(component_id='battery-soc-graph', component_property='extendData')],
              [Input('batterysoc_interval', 'n_intervals')])
def update_data(n):
  returned_data = []
  try:
    for graph in graphs_list:
      if graph['title'] in ("Battery SOC"):
        graph['X'] = datetime.now().strftime("%H:%M:%S")
        #graph['Y'] = mqtt.data_dict[graph["data_key"]]
        graph['Y'] = (random.randint(0,100))
        returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 15])
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
  #   return returned_data
  # except Exception as e:
  #   print(e)  

@app.callback([Output(component_id='XYZ-Linear-Acceleration', component_property='extendData')],
              [Input('XYZlinear-interval', 'n_intervals')])
def update_xyz_linear_acc(n):
  returned_data = []
  try:
    graph = graphs_list[3]
    graph['X'] = datetime.now().strftime("%H:%M:%S")
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    graph['Y'] = (random.randint(0,100))
    returned_data = [[dict(x=[[graph['X']],[graph['X']],[graph['X']], [graph['X']]],\
      y=[[graph['Y']],[random.randint(0,100)], [random.randint(0,100)],[random.randint(0,100)]]), [0,1,2,3], 10]]
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='pedal-angle-graph', component_property='extendData')],
              [Input('pedalangle_interval', 'n_intervals')])
def update_pedal_angle(n):
  returned_data = []
  try:
    graph = graphs_list[1]
    graph['X'] = datetime.now().strftime("%H:%M:%S")
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    Y = random.randint(0,100)
    graph['Y'] = Y
    returned_data = [[dict(x=[[graph['X']], [graph['X']], [graph['X']]],\
      y=[[graph['Y']], [1-Y], [random.randint(0,100)]]), [0,1,2], 10]]
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='XYZ-gyroscope-graph', component_property='extendData')],
              [Input('XYZgyroscope-interval', 'n_intervals')])
def update_xyz_linear_acc(n):
  returned_data = []
  try:
    graph = graphs_list[4]
    graph['X'] = datetime.now().strftime("%H:%M:%S")
    #graph['Y'] = mqtt.data_dict[graph["data_key"]]
    graph['Y'] = (random.randint(0,100))
    returned_data = [[dict(x=[[graph['X']],[graph['X']],[graph['X']], [graph['X']]],\
      y=[[graph['Y']],[random.randint(0,100)], [random.randint(0,100)],[random.randint(0,100)]]), [0,1,2,3], 10]]
    return returned_data
  except Exception as e:
    print(e)  

@app.callback([Output(component_id='gauge', component_property='value')],
              [Input('graph-interval-1', 'n_intervals')])
def update_gauge(n):
    value_out = random.randint(0,100)
    return [value_out]

@app.callback(Output('battery-temp-value', 'children'),
              [Input('battery-temp-store', 'data')])
def update_battery_temp_value(data):
  #return '{} °C'.format(data[(len(data))-1])
  return f"{data[(len(data))-1]} °C"

@app.callback(Output('battery-voltage-value', 'children'),
              [Input('battery-voltage-store', 'data')])
def update_battery_voltage_value(data):
  return '{} V'.format(data[(len(data))-1])
