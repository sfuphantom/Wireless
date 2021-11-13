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
        dbc.Col(GraphComponent("Battery Temperature", "battery-temp-graph", "graph-interval-1", '°C'), 
          width=6, className='col_margin'),
        dbc.Col(GraphComponent("Battery Voltage", "battery-voltage-graph", 'graph-interval-1', "Voltage (V)"), 
          width=3, className='col_margin'),
        ]),
        )
])