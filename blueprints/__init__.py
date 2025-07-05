from .create import create_page_bp, create_api_bp
from .user import user_page_bp, user_api_bp
from .dashboard import dashboard_page_bp, dashboard_api_bp

__all__ = [
    'create_page_bp',
    'user_page_bp',
    'dashboard_page_bp',
    'create_api_bp',
    'user_api_bp',
    'dashboard_api_bp',
]

"""
问题：根据蓝图注册顺序不同，模板（html）名称相同的情况下，可能导致视图返回的模板是同一个（因为名称相同）
    解决方式：
        每个蓝图，模板文件夹内创建一个子文件夹存放html文件（模板），将每个蓝图的模板进行区分，在导入时 子文件/模板文件.html 这样区分（如 dashboard/todos.html、admin/todos.html），调用时带上前缀。
"""
