import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

import pages.Page2.page2_callbacks
from components.stop import StopButton
from components.gauge import Gauge
from components.logo import logo
from components.graph_component import GraphComponent
from components.interval import graphInterval

layout = html.Div(children=[

dcc.Interval(id='graph-interval-1', interval=1000*1),

  html.Div(children=[
    logo(),
    html.Div('Team Phantom', className="app-header", style={'dispay':'inline-block'}),
    ]),

  html.Div(dbc.Row([
    html.Label('PHANTOM 1 ANALYTICS', className='app-title', style={'width':'80%'}), 
    html.Div(StopButton())], justify='around')), 
    
  html.Br(),
  html.Div(dbc.Row([
    dbc.Col(html.Div([
      GraphComponent("Battery Temperature", "battery-temp-graph", 'batterytemp-int', 'batterytemp-rate', False, "graph-interval-1", '°C'), 
      graphInterval('batterytemp-interval'),
    ]), width=6, className='col_margin'),
    dbc.Col(html.Div([
      GraphComponent("Battery Voltage", "battery-voltage-graph", 'batteryvoltage-int', 'batteryvoltage-rate', False, 'graph-interval-1', "Voltage (V)"), 
      graphInterval('batteryvoltage-interval'),        
    ]), width=3, className='col_margin'),
  ]),)
])