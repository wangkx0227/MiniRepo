from flask import Flask
from blueprints.authentication.app import user_bp
from blueprints.dashboard.app import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    return app
