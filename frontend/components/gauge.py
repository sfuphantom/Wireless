import dash_daq as daq
import dash_html_components as html

def Gauge(input, style={}):
    return html.Div( 
        daq.Gauge(
        min=0,
        max=150,
        value=input,
        showCurrentValue=True,
        units="Km/h",
        label='Speed',
        color= "#ffa600",
        style ={'backgroundColor':'#262626'}
    )
)