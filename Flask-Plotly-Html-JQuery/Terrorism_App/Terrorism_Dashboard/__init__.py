from flask import Flask

def init_app():
    app = Flask(__name__)

    with app.app_context():

        from Terrorism_Dashboard.core.views import core
        from Terrorism_Dashboard.data.views import data
        from Terrorism_Dashboard.eventCharts.views import eventCharts
        from Terrorism_Dashboard.timeSeries.views import timeSeries
        from Terrorism_Dashboard.worldMap.views import worldMap
        app.register_blueprint(core)
        app.register_blueprint(data)
        app.register_blueprint(eventCharts)
        app.register_blueprint(timeSeries)
        app.register_blueprint(worldMap)

        return app
