from .app import dashboard_bp
from .views import workbenches, projects, groups, merge_requests, todos, user_setting, secured_setting, \
    workbenches_overview, workbenches_warehouse,workbenches_analysis,workbenches_fragment

dashboard_bp.add_url_rule('/workbenches', view_func=workbenches, methods=['GET'])

dashboard_bp.add_url_rule('/workbenches/overview', view_func=workbenches_overview, methods=['GET'])
dashboard_bp.add_url_rule('/workbenches/warehouse', view_func=workbenches_warehouse, methods=['GET'])
dashboard_bp.add_url_rule('/workbenches/analysis', view_func=workbenches_analysis, methods=['GET'])
dashboard_bp.add_url_rule('/workbenches/fragment', view_func=workbenches_fragment, methods=['GET'])

dashboard_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
dashboard_bp.add_url_rule('/groups', view_func=groups, methods=['GET'])
dashboard_bp.add_url_rule('/merge_requests', view_func=merge_requests, methods=['GET'])
dashboard_bp.add_url_rule('/todos', view_func=todos, methods=['GET'])
dashboard_bp.add_url_rule('/setting/user_setting', view_func=user_setting, methods=['GET'])
dashboard_bp.add_url_rule('/setting/secured_setting', view_func=secured_setting, methods=['GET'])
