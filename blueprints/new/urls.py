from .app import new_page_bp, new_api_bp, new_api
from .views import projects, groups, snippets

new_page_bp.add_url_rule('/projects', view_func=projects, methods=['GET']) # 新建项目
new_page_bp.add_url_rule('/groups', view_func=groups, methods=['GET']) # 群组
new_page_bp.add_url_rule('/snippets', view_func=snippets, methods=['GET']) # 代码片段
