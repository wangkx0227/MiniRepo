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
    url_path = request.path  # 当前访问的路由
    endpoint = request.endpoint  # 当前访问路由的视图名称
    filter_url_list = app.config["FILTER_URL_LIST"]
    # 静态文件和无效路由过滤
    if endpoint is None or endpoint == 'static' or endpoint.endswith('.static'):
        return
    print(url_path)
    # 过滤指定的路由
    if url_path in filter_url_list:
        return
    original_url = request.full_path  # 原url
    # 如果路由尾部时?说明没有携带get参数,直接分解获取url携带.
    if original_url.endswith("?"):
        original_url = original_url.split("?")[0]
    # 如果用户凭证到期,进行重新登录,携带最后访问的页面url
    # return redirect(url_for("login", get_url=original_url))


# 错误页面403
@app.route("/error/403")
def error_403():
    page_show_status = True  # 用当前值控制侧边栏展示与侧边栏按钮是否可以正常点击
    return render_template("error/403.html", page_show_status=page_show_status)


# 错误页面404
@app.route("/error/404")
def error_404():
    page_show_status = True
    return render_template("error/404.html", page_show_status=page_show_status)


# 首页
@app.route("/")
def index():
    return redirect(url_for("dashboard.workbenches", tab="overview"))


# 登录页
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
