import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

import pages.home.home_callbacks
from components.graph_component import GraphComponent
from components.stop_button import StopButton
from components.graduated_bar import GraduatedBar
from components.gauge import Gauge

figure = dict(data=[{'x': [], 'y': []}], layout=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))

layout = html.Div(style={'backgroundColor': '#3A3A3A', 'color': '#3A3A3A', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'},
#style={'backgroundColor': '#3A3A3A'}, 
children = [
  # first row
  html.Div(dbc.Row([
    # first column of first row
    dcc.Interval(id='graph-interval-1', interval=1000),
    GraphComponent("Acceleration on X-axis", "live-graph-1", "graph-interval-1", style={"marginLeft":"1%"}),
    GraphComponent("Acceleration on Y-axis", "live-graph-2", "graph-interval-1"),
    GraphComponent("Acceleration on Y-axis", "live-graph-3", "graph-interval-1"),

  ], no_gutters=True)),

  html.Div(dbc.Row([
    # first column of first row
 
    GraphComponent("Angular Acceleration on Y-axis", "live-graph-4", "graph-interval-1", style={"marginLeft":"1%"}),
    html.Div(children=[
      StopButton(),
      GraduatedBar(3.5, 'horizontal'),
    ], style={'width':'32%', 'height': '32%','display':'inline-block', 'textAlign': 'center', 'marginTop':'0.5%', 'marginLeft':'.2%'}),
    GraphComponent("Angular Acceleration on Y-axis", "live-graph-5", "graph-interval-1", style={"marginLeft":".4%"}),   
  ], no_gutters=True)), 

  html.Div(dbc.Row([
    # third row
    Gauge(109)
    
  ], style={'marginTop':'0.5%', 'marginLeft': '1%'}, no_gutters=True)), 
])

