import dash_daq as daq
import dash_html_components as html

def ledDisplay(input, text):
    return html.Div(daq.LEDDisplay(
    label=(text),
    value=input,
    color="#FF5E5E",
    backgroundColor="#545454",
    )
)