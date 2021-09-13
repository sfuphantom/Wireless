import dash_html_components as html

def StopButton():
  return html.Div(
    html.Div(children=[html.Img(src='/assets/stop_button.png',  
             style={'height':'20%', 'width':'20%'}, id='stop-button'),
             html.Div(id='out', children='Press button to stop vehicle', style={'color': 'orange'})],
             style = {'textAlign':'center'}
            )
  )