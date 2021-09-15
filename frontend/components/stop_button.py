import dash_html_components as html

def StopButton(style={}):
  return html.Div(children=[html.Img(src='/assets/stop_button.png',  
                  style={'height':'100%', 'width':'100%'}, id='stop-button')],
             style = style
            
  )