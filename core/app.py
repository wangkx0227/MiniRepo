from flask import Flask,redirect, url_for
from blueprints import user_bp, dashboard_bp, new_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    return app


app = create_app()


@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches"))