import redis
from flask_session import Session
from flask import Flask, redirect, url_for, jsonify
from blueprints import user_bp, dashboard_bp, new_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config.from_pyfile("config.py")
    app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379, db=0)
    Session(app)
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)

    return app


app = create_app()


@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches", tab="overview"))


@app.route("/health")
def health_check():
    """健康检查"""
    checks = {
        "ProjectStatus": True,
        "Resource": {
            "MySQL": {
                "Version": "5.7.31",
                "Status": True,
                "Message": ""
            },
            "Redis": {
                "Version": "5.0.14.1",
                "Status": True,
                "Message": "",
            },
        }
    }
    status = 200
    return jsonify(checks), status
