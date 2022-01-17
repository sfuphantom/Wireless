import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from utils.constants import home_page_location, page_2_location, page_3_location

from pages.home import home
from pages.Page2 import Page2
from pages.Page3 import Page3

@app.callback(
  Output("page-content", "children"), 
  Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    # If the user tries to reach a different page, return a 404 message
    if pathname == page_2_location:
        return Page2.layout
    if pathname == page_3_location:
        return Page3.layout
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )