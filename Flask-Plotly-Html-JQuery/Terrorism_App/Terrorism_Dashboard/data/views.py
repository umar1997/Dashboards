# Terrorism_Dashboard/data/views.py
from flask import render_template, url_for, Blueprint

data = Blueprint('data',__name__)

@data.route('/data')
def show():
    return render_template('data.html')
