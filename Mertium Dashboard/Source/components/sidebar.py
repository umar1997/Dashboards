import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

SidebarHeader = dbc.Row(
    [
        dbc.Col(html.H2("Mertium Dashboard")),
        dbc.Col(
            [
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    style={
                        "color": "white",
                        "border-color": "white",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    style={
                        "color": "white",
                        "border-color": "white",
                    },
                    id="sidebar-toggle",
                ),
            ],
            width="auto",
            align="center",
        ),
    ]
)

SidebarLinks = html.Div(
    [
        SidebarHeader,
        html.Hr([], style = {
            'border-color': 'white'
        }),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Count Overview", href="/count-overview", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Score Overview", href="/score-overview", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Articles Time Series", href="/article-timeseries", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Content Time Series", href="/content-timeseries", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Scores Time Series", href="/scores-timeseries", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Articles Analyzed", href="/articles-analyzed", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Articles Selected", href="/articles-selected", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Aggregated Topics", href="/aggregated-topics", active="exact", style = {'color':'#ffbf00'}),
                    dbc.NavLink("Trending Topics", href="/trending-topics", active="exact", style = {'color':'#ffbf00'}),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
    style = {
        'background-color':'#171c26',
        'color':'#ffbf00'
    }
)


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open