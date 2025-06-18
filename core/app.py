from flask_session import Session
from flask import Flask, redirect, url_for

# core包
from .views import index, error_403, error_404, health_check, login
from .public import save_routes_to_redis
from .filters import do_date_differ
from .hooks import register_hooks
# 外部导入包
from resource import redis_link
from blueprints import user_bp, dashboard_bp, new_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config.from_pyfile("config.py")
    app.config['SESSION_REDIS'] = redis_link
    Session(app)
    # 注册蓝图
    app.register_blueprint(new_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(dashboard_bp)
    # 注册全局视图路由
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/login', view_func=login, methods=['GET'])
    app.add_url_rule('/error/403', view_func=error_403, methods=['GET'])
    app.add_url_rule('/error/404', view_func=error_404, methods=['GET'])
    app.add_url_rule('/health_check', view_func=health_check, methods=['GET'])
    # 存储项目下的全部url
    save_routes_to_redis(app)
    # 注册钩子,需要在存储url路由之后
    register_hooks(app)
    # 注册过滤器
    app.add_template_filter(do_date_differ, "do_date_differ")
    return app


app = create_app()


# 错误地址直接渲染
@app.errorhandler(403)
def handle_404(e):
    return redirect(url_for("error_403"))


# 错误地址直接渲染
@app.errorhandler(404)
def handle_404(e):
    return redirect(url_for("error_404"))
