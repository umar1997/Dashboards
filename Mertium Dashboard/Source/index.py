import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from components.sidebar import SidebarLinks
from components.countOverview import CountCards
from components.scoreOverview import ScoreCards

URL = dcc.Location(id="url")
Content = html.Div(id="page-content", children=[])

app.layout = html.Div(
    [
    URL, 
    SidebarLinks, 
    Content
    ]
)

@app.callback(Output("page-content", "children"), 
                [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/count-overview":
        return CountCards
    elif pathname == "/score-overview":
        return ScoreCards
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == '__main__':
    app.run_server(port= 9000, debug = True)
