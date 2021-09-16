import dash_daq as daq
import dash_html_components as html

def GraduatedBar (input_value, orientation):
    graduated_bar = daq.GraduatedBar(
       color={"gradient":True,"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
       showCurrentValue=True,
       value=input_value,
       id = 'bar',
       className= 'bar_class',
       label= 'Text',
       style={'backgroundColor': '#262626', 'marginBottom':'5%'})

    if orientation.lower() == "vertical":
        'bar'.vertical=True

    return html.Div(
        graduated_bar)