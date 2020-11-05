# Terrorism_Dashboard/worldMap/views.py
from flask import render_template, request, Blueprint
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

worldMap = Blueprint('worldMap',__name__)

@worldMap.route('/world-map')
def chart():
    return render_template('worldmap.html')
