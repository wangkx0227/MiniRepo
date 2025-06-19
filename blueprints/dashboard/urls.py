from .app import dashboard_page_bp, dashboard_api
from .views import workbenches, projects, groups, merge_requests, todos, user_setting, secured_setting

dashboard_page_bp.add_url_rule('/workbenches', view_func=workbenches, methods=['GET'])
dashboard_page_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
dashboard_page_bp.add_url_rule('/groups', view_func=groups, methods=['GET'])
dashboard_page_bp.add_url_rule('/merge_requests', view_func=merge_requests, methods=['GET'])
dashboard_page_bp.add_url_rule('/todos', view_func=todos, methods=['GET'])
dashboard_page_bp.add_url_rule('/setting/user_setting', view_func=user_setting, methods=['GET'])
dashboard_page_bp.add_url_rule('/setting/secured_setting', view_func=secured_setting, methods=['GET'])
