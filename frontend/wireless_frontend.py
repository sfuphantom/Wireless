import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'components')))
from graph_component import GraphComponent

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

test_graph = GraphComponent({'x':[1,3,5,2,7,8], 'y':[2,4,6,9,3,0]}, "Test",
                           "test-class", "graph-1", "container-1")
test_graph.style = {'width': '40%', 'height': '20%'}

app.layout = html.Div([
  test_graph
], className="container", style={"background-image": "linear-gradient(180deg, blue, lightblue)"})

if __name__ == '__main__':
    app.run_server(debug=True)