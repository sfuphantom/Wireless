import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd

def GraphComponent(data, graph_name, class_name, graph_id, container_id, graph_type="scatter"):
  if graph_type == "scatter":
    fig = px.scatter(data['x'], data['y'],
                    labels={
                             "x": "Time Elapsed",
                             "y": "State of Charge",
                           },
                    title="State of Charge of Battery")

  fig.update_layout(
      margin=dict(l=20, r=20, t=80, b=20)
  )

  return html.Div([
    dcc.Graph(figure=fig, id=graph_id, style={"background-image": "linear-gradient(180deg, blue, lightblue)"})
  ], className=class_name, id=container_id)