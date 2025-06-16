import redis
import json
from flask_session import Session
from flask import Flask, redirect, url_for, jsonify, request, render_template, session

from resource import redis_link
from blueprints import user_bp, dashboard_bp, new_bp


def save_routes_to_redis(f_app):
    """
        存储url
    """
    routes = []
    for rule in f_app.url_map.iter_rules():
        if rule.endpoint == 'static' or rule.endpoint.endswith('.static'):  # 过滤静态路由
            continue
        routes.append({
            "rule": rule.rule,
            "endpoint": rule.endpoint,
            "methods": list(rule.methods)
        })
    # 保存为 JSON 字符串
    redis_link.set(f_app.config["URL_REDIS_KEY"], json.dumps(routes, ensure_ascii=False))


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config.from_pyfile("config.py")
    app.config['SESSION_REDIS'] = redis_link
    Session(app)
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    # 项目下的url存储到redis中
    save_routes_to_redis(app)
    return app


app = create_app()


# 设置请求钩子,处理用户登录状态. -- 全局生效,验证是否存在登录状态
@app.before_request
def before_request():
    # 不做用户凭证验证
    url_path = request.path  # 当前访问的路由
    url_method = request.method  # 当前路由访问方法
    endpoint = request.endpoint  # 当前访问路由的视图名称
    filter_url_list = app.config["FILTER_URL_LIST"]
    # 静态文件和无效路由过滤
    if endpoint is None or endpoint == 'static' or endpoint.endswith('.static'):
        return
    # 过滤指定的路由
    if url_path in filter_url_list:
        return
    if not session.get("user_status"):
        original_url = request.full_path  # 原url
        # 如果路由尾部时?说明没有携带get参数,直接分解获取url携带.
        if original_url.endswith("?"):
            original_url = original_url.split("?")[0]
        # 如果用户凭证到期,进行重新登录,携带最后访问的页面url
        return redirect(url_for("login", get_url=original_url))
    # 路由匹配机制，如果对应不上解析的路由，那么直接就返回404
    routes = redis_link.get(app.config["URL_REDIS_KEY"])
    adapter = app.url_map.bind("localhost")
    _endpoint, _args = adapter.match(url_path, method=url_method)  # 解析的路由参数与路由视图的名称
    if routes:
        routes = json.loads(routes.decode('utf-8'))
    match_status = False
    for i in routes:
        if i.get("endpoint") == _endpoint:
            match_status = True
    if not match_status:
        return redirect(url_for("error_404"))
    return


# 错误页面403
@app.errorhandler(403)
@app.route("/error/403")
def error_403():
    page_show_status = True  # 用当前值控制侧边栏展示与侧边栏按钮是否可以正常点击
    return render_template("error/403.html", page_show_status=page_show_status)


# 错误页面404
@app.errorhandler(404)
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
    session["user_status"] = "asdasdasdwxc312313asdqe"  # 默认登录状态
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
