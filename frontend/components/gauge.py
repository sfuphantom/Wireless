import dash_daq as daq
import dash_html_components as html

def Gauge(input):
    return html.Div( 
        daq.Gauge(
        min=0,
        max=150,
        value=input,
        units="Km/h",
        label='Speed',
        size=150,
        color='rgb(255, 94, 94)'
    )
)