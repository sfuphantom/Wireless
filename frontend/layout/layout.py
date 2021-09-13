import dash_html_components as html
import dash_core_components as dcc

from layout.sidebar.sidebar import sidebar

dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"), sidebar, content])