import numpy as np
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        #     'https://fonts.googleapis.com/css?family=Lato'
        # ]
    )

    dash_app.layout = html.Div(children = [
    html.H1('Dash'),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id = 'Example',
             figure = {'data':[{'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                               {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'NYC'}
                              ],
                      'layout': {'title':'Bar Plots'}
                      })
    ])
    return dash_app.server 
