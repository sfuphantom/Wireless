import dash
import dash_bootstrap_components as dbc

from utils.external_assets import FONT_AWSOME, CUSTOM_STYLE
from layout.layout import layout

import flask
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mqtt_handler import *

FRONTEND_NAME = "Frontend"
MQTT_BROKER_IP = "78da1aca5bac48ceb4c9d7eff3de95e9.s1.eu.hivemq.cloud"

#mqtt = MqttHandler(FRONTEND_NAME, MQTT_BROKER_IP)

server = flask.Flask(__name__) # define flask app.server

app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        FONT_AWSOME,
        CUSTOM_STYLE
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

app.layout = layout

server = app.server