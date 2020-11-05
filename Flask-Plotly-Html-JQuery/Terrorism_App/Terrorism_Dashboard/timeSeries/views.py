# Terrorism_Dashboard/timeSeries/views.py
from flask import render_template, request, Blueprint
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

timeSeries = Blueprint('timeSeries',__name__)

df = pd.read_csv("./Terrorism_Dashboard/static/data/Terrorism_data.csv",encoding='latin1')
df['Date'] = pd.to_datetime(df['Date'])
dfx = df.copy(deep=False)

@timeSeries.route('/time-series')
def chart():
    time_span, country = 'Year', 'All'
    graph = create_plot(time_span, country)
    dx = dfx[['country_txt']].sort_values('country_txt')
    country_list = list(dx['country_txt'].unique())
    return render_template('time.html', plot=graph,country_list = country_list)


def create_plot(time_span, country):
    if country == 'All':
        if time_span == "Decade":
            dx = dfx.groupby((dfx['Date'].dt.year//10)*10).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Year":
            dx = dfx.groupby(dfx['Date'].dt.year).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Month":
            dx = dfx.groupby(dfx['Date'].dt.month).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Day":
            dx = dfx.groupby(dfx['Date'].dt.day).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "WeekDay":
            weekdayDict = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            dx = dfx.groupby(dfx['Date'].dt.weekday).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
            dx.index = weekdayDict
    else:
        if time_span == "Decade":
            dx = dfx[dfx['country_txt']==country].groupby((dfx['Date'].dt.year//10)*10).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Year":
            dx = dfx[dfx['country_txt']==country].groupby(dfx['Date'].dt.year).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Month":
            dx = dfx[dfx['country_txt']==country].groupby(dfx['Date'].dt.month).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "Day":
            dx = dfx[dfx['country_txt']==country].groupby(dfx['Date'].dt.day).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
        elif time_span == "WeekDay":
            weekdayDict = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            dx = dfx[dfx['country_txt']==country].groupby(dfx['Date'].dt.weekday).agg('count').rename(columns={"country_txt": "Count Of Events"})[['Count Of Events']]
            dx.index = weekdayDict

    trace = go.Scatter(
    x = dx.index,
    y = dx['Count Of Events'],
    mode = 'lines+markers',
    name = 'Yearly',
    marker = {
            'size': 8,
            'color': 'rgb(51,204,153)',
            'line': {'width': 2}
            }
    )
    graphs = {
        'data' : [trace],
        'layout' : go.Layout(
        title = 'Terrorism Events',
        xaxis = {'title': time_span+"s"},
        yaxis = {'title': '# of Events'},
        hovermode='closest')
    }

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@timeSeries.route('/series', methods=['GET', 'POST'])
def change_features():

    time_span = request.args['time_selected']
    country = request.args['country_selected']
    print(country)
    graphJSON = create_plot(time_span, country)
    return graphJSON
