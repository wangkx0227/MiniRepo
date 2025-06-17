import json
from flask_session import Session
from flask import Flask, redirect, url_for, request, session

# core包
from .views import index, error_403, error_404, health_check
from .public import save_routes_to_redis, register_filters, redis_link
# 外部导入包
from blueprints import user_bp, dashboard_bp, new_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config.from_pyfile("config.py")
    app.config['SESSION_REDIS'] = redis_link
    Session(app)
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    # 注册全局视图路由
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/error/403', view_func=error_403, methods=['GET'])
    app.add_url_rule('/error/404', view_func=error_404, methods=['GET'])
    app.add_url_rule('/health_check', view_func=health_check, methods=['GET'])
    # 存储项目下的全部url
    save_routes_to_redis(app)
    # 注册过滤起
    register_filters(app)
    return app


app = create_app()


# 设置请求钩子,处理用户登录状态. -- 全局生效,验证是否存在登录状态
@app.before_request
def before_request():
    """
        作用：
            1.路由验证
            2.路由过滤
            3.登录凭证验证
    """
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
    # 凭证验证
    if not session.get("user_status"):
        original_url = request.full_path  # 原url
        # 如果路由尾部时?说明没有携带get参数,直接分解获取url携带.
        if original_url.endswith("?"):
            original_url = original_url.split("?")[0]
        # 如果用户凭证到期,进行重新登录,携带最后访问的页面url
        return redirect(url_for("login", get_url=original_url))
    # 路由验证
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
    print(session.get("user_status"))
    return


# 错误地址直接渲染
@app.errorhandler(403)
def handle_404(e):
    return redirect(url_for("error_403"))


# 错误地址直接渲染
@app.errorhandler(404)
def handle_404(e):
    return redirect(url_for("error_404"))
