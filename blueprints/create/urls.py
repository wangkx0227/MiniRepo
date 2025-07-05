from .app import create_page_bp, create_api_bp, create_api
from .views import projects, groups, snippets

create_page_bp.add_url_rule('/projects', view_func=projects, methods=['GET']) # 新建项目
create_page_bp.add_url_rule('/groups', view_func=groups, methods=['GET']) # 群组
create_page_bp.add_url_rule('/snippets', view_func=snippets, methods=['GET']) # 代码片段
