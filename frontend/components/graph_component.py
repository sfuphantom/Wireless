import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def GraphComponent(graph_name, graph_id, interval_id, y_axis_title, style={}, data={'x':[], 'y':[]}, graph_type="scatter", update_interval=1000):
  if graph_type == "scatter":
    fig = go.Figure()
    fig.add_traces(
      go.Scatter(
        x=[],
        y=[],
        name = 'Scatter',
        mode = 'lines', 
        line_color='#ffa600')
    )

    fig.update_layout(
      uirevision='constant',
      paper_bgcolor= '#545454',
      plot_bgcolor = '#545454',
      title = graph_name,
      showlegend=True,
      xaxis=dict(title = 'time (s)', dtick=1, showgrid=False), 
      yaxis=dict(title = y_axis_title),
      font_color = '#FF6361',
      margin={'l': 5, 'b': 10, 'r': 10, 't': 40},
      height=300
    )

  return html.Div(
    #className='data-graph',
    children=[
      dcc.Graph(
        id=graph_id, 
        figure=fig 
      )],
    style=style, className='graph_container'
  )
  