import dash_daq as daq
import dash_html_components as html

def StopButton():
    return html.Div(
        daq.StopButton(
            label='Emergency Shut Off',
            labelPosition='top',
            buttonText='STOP',
            size=120)
            )