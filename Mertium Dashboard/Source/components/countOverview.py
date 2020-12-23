import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

from app import app

dropdown = dbc.Row(
    [ 
        dbc.Col(

        ),
        dbc.Col(

        ),
        dbc.Col(

        ),
        dbc.Col(
            dbc.DropdownMenu(
                id = 'count-dropdown',
                label="Time Filters",
                children=[
                    dbc.DropdownMenuItem("Last Hour", id='hour'),
                    dbc.DropdownMenuItem("Last 24 Hours", id='day'),
                    dbc.DropdownMenuItem("Last 7 days", id='week'),
                    dbc.DropdownMenuItem("Last 30 days", id='month'),
                    dbc.DropdownMenuItem("Last year", id='year'),
                ],
                right = True,
            )
        ),
    ]
)

@app.callback(Output('count-dropdown', 'label'),
            [Input('hour', 'n_clicks'), Input('day', 'n_clicks'), Input('week', 'n_clicks'),
                Input('month', 'n_clicks'), Input('year', 'n_clicks')]
)
def update_label(n1, n2, n3, n4, n5):
    id_lookup = {
        'hour': 'Last Hour',
        'day': 'Last 24 Hours',
        'week': 'Last 7 days',
        'month': 'Last 30 days',
        'year': 'Last Year',
    }

    ctx = dash.callback_context
    if (n1 is None and n2 is None and n3 is None and n4 is None and n5 is None) or not ctx.triggered:
        return "Time Filters"
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    return id_lookup[button_id]


card_headers = ['Null Image Articles', 'Null Author Articles', 'Null News Source Articles']
card_percentages = [13, 15, 26]
card_colours = ['primary', 'warning', 'danger']

def card_content(header, percentage):
    card = [
        dbc.CardHeader(header),
        dbc.CardBody(
            [
                html.H3(str(percentage) + '%', className="card-title", style={'textAlign': 'center'}),
            ]
        ),
    ]
    return card

cards = dbc.Row(
            [dbc.Col(dbc.Card(card_content(card_headers[i], card_percentages[i]), color=card_colours[i], inverse=True)) for i in range(len(card_headers))],
            className="card-list",
        )


newsSourceGraph = dcc.Graph(
    id='newsSource-barchart',
    figure = {
        'data' : [go.Bar(
            x = ['Wall Street Journal', 'Bloomberg', 'MarketWatch'],
            y = [20, 49, 17],
        )],
        'layout' : go.Layout(
            title = 'News Source Percentages',
            xaxis = {'title' : 'News Sources'},
            yaxis = {'title' : 'Percentage %'},
            hovermode='closest',
        )
    }
)



CountCards = html.Div(
    [
        dropdown,
        html.Br(),
        cards,
        newsSourceGraph,
    ]
)