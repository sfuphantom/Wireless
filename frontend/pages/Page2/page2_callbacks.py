import dash
from dash.dependencies import Input, Output, State 
import dash_daq

import plotly.express as px
import plotly.graph_objs as go
from app import app, mqtt
from utils.constants import graphs_list
import pages.store_callbacks

from datetime import datetime
import pandas as pd
import time

import random
import numpy as np

@app.callback([Output(component_id='battery-temp-graph', component_property='extendData')],
              Input('battery-temp-store', 'data'))
def update_battery_temp_graph(data):
  print("update data")
  returned_data = []
  try:
    for graph in graphs_list:
      if graph['title'] == "Battery Temperature":
        graph['X'] =  data[(len(data))-2]
        graph['Y'] = data[(len(data))-1]
        returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 15])
        #print(returned_data)
    return returned_data
  except Exception as e:
    print(e)

@app.callback([Output(component_id='battery-voltage-graph', component_property='extendData')],
              Input('battery-voltage-store', 'data'))
def update_battery_voltage_graph(data):
  print("update data")
  returned_data = []
  try:
    for graph in graphs_list:
      if graph['title'] == "Battery Voltage":
        graph['X'] =  data[(len(data))-2]
        graph['Y'] = data[(len(data))-1]
        returned_data.append([dict(x=[[graph['X']]], y=[[graph['Y']]]), [0], 15])
    return returned_data
  except Exception as e:
    print(e)


#add function that creates graph with values from stored data upon tab switch 
