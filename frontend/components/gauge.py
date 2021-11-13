import dash_daq as daq
import dash_html_components as html

def Gauge(gauge_id):
    return html.Div( 
        daq.Gauge(
        id = gauge_id,
        min=0,
        max=150,
        units="Km/h",
        label='Speedometer',
        size=150,
        #color='rgb(255, 94, 94)',
        color={"gradient":True,"ranges":{"green":[0,90],"yellow":[90,120],"red":[120,150]}},
    )
)