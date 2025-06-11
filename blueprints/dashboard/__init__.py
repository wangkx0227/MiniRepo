from .urls import dashboard_bp

__all__ = ['dashboard_bp']



"""
blueprints
    ├── authentication/
        ├── __init__.py    # 只暴露 user_bp
        ├── views.py       # 定义视图
        ├── urls.py       # 定义路由
    ├── dashboard/
        ├── __init__.py    # 只暴露 dashboard_bp
        ├── views.py       # 定义所有路由和视图
        ├── urls.py       # 定义路由
core
    ├── app.py # flask对象位置，需要注册蓝图
"""