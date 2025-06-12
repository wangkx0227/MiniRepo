import redis
from datetime import timedelta
from flask_session import Session
from flask import Flask, redirect, url_for
from blueprints import user_bp, dashboard_bp, new_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config.from_pyfile("config.py")
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2) # session的过期时间
    app.config['SESSION_REDIS'] = redis.Redis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        db=app.config['REDIS_DB']
    )
    Session(app)
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    return app


app = create_app()


@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches"))
