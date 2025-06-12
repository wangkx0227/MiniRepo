from .app import app as run_app
from .cache import redis_link

__all__ = ["run_app", "redis_link"]

"""
blueprints
    ├── authentication/
        ├── __init__.py    # 只暴露 user_bp
        ├── views.py     
        ├── urls.py      
    ├── dashboard/
        ├── __init__.py    # 只暴露 dashboard_bp
        ├── views.py       
        ├── urls.py      
core
    ├── __init__.py  # 暴露 app对象和redis对象
    ├── app.py 
    ├── config.json 
    ├── config.py 
    ├── cache.py 
    ├── mysql.py 
templates 
main.py # 运行app对象
"""
