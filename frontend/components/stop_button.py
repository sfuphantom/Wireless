import dash_html_components as html

def StopButton(style={}):
  return html.Div(children=[html.Img(src='/assets/stop_button.png',  
                  style={'height':'100%', 'width':'100%', 'backgroundColor': '#262626', 'marginBottom':'5%'}, id='stop-button')],
             #html.Div(id='out', children='Press button to stop vehicle', style={'color': 'orange'})],
             #style = style
            
  )