import redis
from flask_session import Session
from flask import Flask, redirect, url_for, jsonify, request, render_template
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


# 设置请求钩子,处理用户登录状态. -- 全局生效,验证是否存在登录状态
@app.before_request
def before_request():
    # 不做用户凭证验证
    if request.endpoint == "login" or (
            request.endpoint == 'static'
            or request.endpoint.endswith('.static')
    ):
        return
    original_url = request.full_path  # 原url
    # 如果用户凭证到期,进行重新登录,携带最后访问的页面url
    # return redirect(url_for("login", get_url=original_url))


@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches", tab="overview"))


@app.route("/login")
def login():
    # 获取参数,然后登录成功后,跳转到最后访问页面的url
    next_url = request.args.get("get_url")
    if next_url:
        return redirect(next_url)
    return render_template("login.html")


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
