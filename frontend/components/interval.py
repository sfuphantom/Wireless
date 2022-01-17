import dash_core_components as dcc
import dash_html_components as html

def graphInterval(interval_id):
    return html.Div(dcc.Interval(id=interval_id, interval = 1*1000)
    )
