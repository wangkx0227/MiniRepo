from .app import app as run_app

__all__ = ["run_app"]

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
"""
是不是这个意思
1.main.py 由于导入了 from core import run_app，就执行了core的__init__.py 
2.core的__init__.py 执行了 from .app import app as run_app，引入了app对象（create_app()函数执行）
4.create_app() 函数执行执行了app.config.from_pyfile("config.py")，读取了 core/config.py 配置 同时注册了蓝图
5.app.register_blueprint(dashboard_bp)蓝图内的一个视图导入了 from core import redis_link
6.但是由于 from .cache import redis_link 是在  from core import run_app 的后面，导致它并未实例化，没有加载到内存中没有这个对象。
7.core的__init__.py 执行了 from .cache import redis_link 对redis链接池实（执行）例化对象redis_link
8.redis_link实例对象内部代码 with open(config_file, "r", encoding="utf-8") as f: 读取了core/config.json配置文件
9.完成7和8的操作才会生成对象

"""