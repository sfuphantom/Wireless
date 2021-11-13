import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def GraphComponent(graph_name, graph_id, interval_id, y_axis_title, style={}, data={'x':[], 'y':[]}, graph_type="scatter", update_interval=1000):
  if graph_type == "scatter":
    fig = go.Figure()
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    if graph_name == "GPS":
      fig.add_traces([ go.Scatter(
          x=[],
          y=[],
          name = 'Scatter1',
          mode = 'lines', 
          line_color='#4e2b6c')
        # go.Scatter(
        #   x=[],
        #   y=[],
        #   name = 'Scatter1',
        #   mode = 'lines', 
        #   line_color='#4e2b6c'),
        # go.Scatter(
        #   x=[],
        #   y=[],
        #   name = 'Scatter2',
        #   mode = 'lines', 
        #   line_color='#85f185'),
        # go.Scatter(
        #   x=[],
        #   y=[],
        #   name = 'Scatter3',
        #   mode = 'lines',
        #   line_color='#a367d7'),
        # go.Scatter(
        #   x=[],
        #   y=[],
        #   name = 'Scatter4',
        #   mode = 'lines',             
        #   line_color='#f83195')
        ])
        
    elif graph_name in ["XYZ Linear Acceleration", "XYZ Gyroscope"]:
      fig.add_traces([
        go.Scatter(
          x=[],
          y=[],
          name = 'Displacement',
          mode = 'lines', 
          line_color='#2dd7e9'),
        go.Scatter(
          x=[],
          y=[],
          name = 'Velocity',
          mode = 'lines', 
          line_color='#a265d7'),  
        go.Scatter(
          x=[],
          y=[],
          name = 'Acceleration',
          mode = 'lines', 
          line_color='#ff5e5e')])
      fig.add_trace(
        go.Scatter(
          x=[],
          y=[],
          name = 'Secondary Y',
          mode = 'lines', 
          line_color='black'), secondary_y=True)

      fig.update_yaxes(
        title_text="<b>Second</b> y axis", 
        secondary_y=True)
    
    elif graph_name == 'Pedal Angle':
      fig.add_traces([
        go.Scatter(
          x=[],
          y=[],
          name = 'Brake',
          mode = 'lines', 
          line_color='#a265d7'),
        go.Scatter(
          x=[],
          y=[],
          name = 'Accelerator',
          mode = 'lines', 
          line_color='#ff5e5e')
      ])
      fig.add_trace(
        go.Scatter(
          x=[],
          y=[],
          name = 'X Acceleration',
          mode = 'lines', 
          line_color='black'), secondary_y=True)
      fig.update_yaxes(
        title_text="<b>X Acceleration</b> in m/s2", 
        secondary_y=True)

    else: 
      fig.add_traces([
        go.Scatter(
          x=[],
          y=[],
          name = 'Test',
          mode = 'lines', 
          line_color='#a265d7')])
      
    fig.update_layout(
      uirevision='constant',
      paper_bgcolor= '#d3d3d3',
      plot_bgcolor = '#d3d3d3',
      title = graph_name,
      showlegend=True,
      xaxis=dict(title = 'time (s)', dtick=1,),# showgrid=False), 
      yaxis=dict(title = y_axis_title),
      font_color = '#4e2b6c',
      #legend_itemsizing='constant',
      #legend_orientation='h',
      legend={"orientation": "h",'xanchor': "center",'y': -.3,'x': 0.5},
      margin={'l': 1, 'b': 10, 'r': 1, 't': 40},
      height=300,
      font=dict(
        size=10))

    if graph_name == 'GPS':
        fig.update_layout(xaxis=dict(title = 'Longitude', dtick=1,))

    if graph_name == 'Pedal Angle':
      fig.update_layout(height=200)
  return html.Div(
    #className='data-graph',
    children=[
      dcc.Graph(
        id=graph_id, 
        figure=fig 
      )],
    style=style, className='graph_container'
  )
  