from frontend.components.leddisplay import ledDisplay
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

import pages.home.home_callbacks
from components.graph_component import GraphComponent
from components.stop import StopButton
from components.gauge import Gauge
from components.logo import logo

figure = dict(data=[{'x': [], 'y': []}], layout=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))

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

 #div for battery components 
  html.Div(children=[(dbc.Row([
    dbc.Col(html.Div(children=[
      html.H4("Battery Temperature"), 
      html.H5(('00'), style={'color':'orange'})], className="mini_container"), 
      width=2, className='col_margin'),
      
    dbc.Col(html.Div(children=[
      html.H4('Battery Current'), 
      html.H5(('00'), style={'color':'red'})], className="mini_container"), 
      width=2, className='col_margin'),
    dbc.Col(html.Div(children=[
      html.H4('Battery Voltage'), 
      html.H5(('00'), style={'color':'green'})], className="mini_container"), 
      width=2, className='col_margin'),

    dbc.Col(html.Div(children=[
      html.H4('Shock Travel'), 
      html.H5(('00'), style={'color':'blue'})], className="mini_container"), 
      width=2, className='col_margin'),
    dbc.Col(html.Div(ledDisplay(123, 'Speed of Vehicle'), className="mini_container"), width=4, className='col_margin')
    ])),

    html.Div(dbc.Row([
      dbc.Col(GraphComponent("Battery SOC", "live-graph-1", 'graph-interval-1', "%"), 
      width=4, className='col_margin'),
      dbc.Col(GraphComponent('Brake Pedal Angle', "live-graph-2", "interval-component", 'Brake Pedal Position'), 
      width=4, className='col_margin'),

      dbc.Col(html.Div(children=[
      html.H4("Wheel Speeds"), 
      html.H5(('60'), style={'color':'orange'})], className="wheel_container"), 
      width=4, className='col_margin'),
      ]),
      )]),

  html.Div(dbc.Row([
    dbc.Col(GraphComponent("GPS", "live-graph-3", "graph-interval-1", 'Position Z'), 
    width=6, className='col_margin'),
    dbc.Col(GraphComponent("XYZ Linear Acceleration", "live-graph-4", "graph-interval-1", 'XYZ'), 
    width=3, className='col_margin'),
    dbc.Col(GraphComponent("XYZ Gyroscope", "live-graph-5", "graph-interval-1", 'XYZ'), 
    width=3, className='col_margin')])
  )])