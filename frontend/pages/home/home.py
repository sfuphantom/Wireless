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
from components.interval import graphInterval

figure = dict(data=[{'x': [], 'y': []}], layout=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))

layout = html.Div(children=[

  dcc.Interval(id='graph-interval-1', interval=1000*1),

  html.Div(children=[
    logo(),
    html.Div('Team Phantom', className='app-header', style={'dispay':'inline-block'}),
    ]),

  html.Div(dbc.Row([
    html.Label('PHANTOM 1 ANALYTICS', className='app-title', style={'width':'80%'}), 
    html.Div(StopButton())], justify='around')), 
    
  html.Br(),

 #div for battery components 
  html.Div(children=[(dbc.Row([
    
    dbc.Col(html.Div([ 
      dbc.Row([dbc.Col(html.Div(children=[
        html.Tr("Front Left"),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')]),
      dbc.Row([dbc.Col(html.Div(children=[
        html.Tr("Back Left"),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')]),  
        ]), width = 2),
    dbc.Col(html.Div([
      dbc.Row([dbc.Col(html.Div(children=[
        html.Tr("Front Right"),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')]),  
      dbc.Row([dbc.Col(html.Div(children=[
        html.Tr("Back Right"),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')])
    ]), width = 2),
    dbc.Col(html.Div([
      dbc.Row([dbc.Col(html.Div(children=[
        html.H4(("Tire Temp"), style = {'font-size':'15px'}),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')]),  
      dbc.Row([dbc.Col(html.Div(children=[
        html.H4(("N/A"), style = {'font-size':'15px'}),
        html.H4(('00'), style={'color':'#a265d7'})], className="mini_container2"), 
        style={}, className='col_margin')])
    ]), width = 2),
    dbc.Col(html.Div(), width=3),
    # dbc.Col(GraphComponent('Pedal Angle', "live-graph-2", True, "interval-component", 'Pedal Position'), 
    #   width=4, className='col_margin'),
    dbc.Col(html.Div(Gauge('gauge')), style={'align':'center'}, width = 3),
    ])),

    html.Div(dbc.Row([
      # dbc.Col(GraphComponent("GPS", "live-graph-3", False, "graph-interval-1", 'Latitude'), 
      #   width=6, className='col_margin'),
      dbc.Col(html.Div([
        GraphComponent('Pedal Angle', "pedal-angle-graph", 'pedalangle-int','pedalangle-rate', True, 'Pedal Position'),
        graphInterval('pedalangle_interval')
      ]), width=6, className='col_margin'),
      dbc.Col(html.Div([
        GraphComponent("Battery SOC", "battery-soc-graph", 'batterySOC-int','batterySOC-rate', False, "%"), 
        graphInterval('batterysoc_interval')
      ]), width=3, className='col_margin'),

      dbc.Col(html.Div([
        dbc.Row([dbc.Col(html.Div(children=[
          html.H4("Battery Temperature", style={'font-size':'15px'}), 
          html.H4(id='battery-temp-value', style={'color':'#c492f0', 'font-size':'20px'})], className="mini_container2"), 
          style={}, className='col_margin')]),
        dbc.Row([dbc.Col(html.Div(children=[
          html.H4("Battery Voltage", style={'font-size':'15px'}), 
          html.H4(id='battery-voltage-value', style={'color':'#c492f0', 'font-size':'20px'})], className="mini_container2"), 
          style={}, className='col_margin')]),
        dbc.Row([dbc.Col(html.Div(children=[
          html.H4("Battery Current"), 
          html.H4(('00'), style={'color':'#a265d7', 'font-size':'15px'})], className="mini_container2"), 
          style={}, className='col_margin')])
        ])),
      ]),
      )]),

  html.Div(dbc.Row([
    dbc.Col(html.Div([
      GraphComponent("XYZ Gyroscope", "XYZ-gyroscope-graph", 'XYZgyroscope-int', 'XYZgyroscope-rate', True, 'Degrees/Sec'), 
      graphInterval('XYZgyroscope-interval'),
      ]), width=6, className='col_margin'),
    dbc.Col(html.Div([
      GraphComponent("XYZ Linear Acceleration", "XYZ-Linear-Acceleration", 'XYZlinear-int', 'XYZlinear-rate', True, 'm/s2'), 
      graphInterval('XYZlinear-interval'),
      ]), width=6, className='col_margin')
    ])),
])
