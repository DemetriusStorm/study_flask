import dash
import dash_core_components as dcc
import dash_html_components as html
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
rnd_xy = range(random.randrange(0, 25))

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [x for x in range(random.randrange(2, 35))], 'y': [y for y in rnd_xy], 'type': 'bar', 'name': 'SF'},
                {'x': [x for x in range(random.randrange(1, 25))], 'y': [y for y in rnd_xy], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
