import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

import pages.home.home_callbacks
from components.graph_component import GraphComponent

layout = html.Div(style={'backgroundColor': '#3A3A3A', 'color': '#3A3A3A', 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'},
#style={'backgroundColor': '#3A3A3A'}, 
children = [
  html.H1(children="Wireless GUI",style={'text-align':'center', 'color':'#FF6361'}),
  # first row
  html.Div(dbc.Row([
    # first column of first row
    GraphComponent("Acceleration on X-axis", "live-graph-1", "graph-interval-1"),
    GraphComponent("Acceleration on Y-axis", "live-graph-2", "graph-interval-1"),
    GraphComponent("Acceleration on Y-axis", "live-graph-3", "graph-interval-1")
    
  ], no_gutters=True)),

  # second row
  html.Div(
    html.Div(children=[html.Img(src='/assets/stop_button.png',  
      style={'height':'20%', 'width':'20%'}, id='stop-button'),
      html.Div(id='out', children='Press button to stop vehicle', style={'color': 'orange'})],
      style = {'textAlign':'center'}))
])
