import dash_html_components as html

def logo():
    return html.Div(html.Img(src='/assets/phantom_logo.png',
        style={'height':'40px', 'width':'40px', 'display':'inline-block'}))
