import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

def GraphComponent(graph_name, graph_id, interval_id, style={}, data={'x':[], 'y':[]}, graph_type="scatter", update_interval=1000):
  if graph_type == "scatter":
    fig = go.Figure()
    fig.add_traces(
      go.Scatter(
        x=[],
        y=[],
        name = 'Scatter',
        mode = 'lines+markers', line_color='#ffa600')
    )

    fig.update_layout(
      uirevision='constant',
      paper_bgcolor= '#262626',
      plot_bgcolor = '#262626',
      title = graph_name,
      xaxis=dict(gridcolor = 'white', title = 'time (s)'), 
      yaxis=dict(gridcolor = 'white', title = 'Acc (m/s2)'),
      font_color = '#FF6361'
    )

  return html.Div(
    className='data-graph',
    children=[
      dcc.Graph(
        id=graph_id, 
        animate=False,
        figure=fig 
      )],
    style=style
  )