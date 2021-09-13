import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd

def GraphComponent(graph_name, graph_id, interval_id, data={'x':[], 'y':[]}, graph_type="scatter", update_interval=1000):
  if graph_type == "scatter":
    fig = px.scatter(data['x'], data['y'],
                    labels={
                             "x": "Time Elapsed",
                             "y": "State of Charge",
                           },
                    title=graph_name)

  return html.Div(
    className='data-graph',
    children=[
      dcc.Graph(
        id=graph_id, 
        animate=False, 
      ),
    dcc.Interval(id=interval_id, interval=update_interval)
  ])