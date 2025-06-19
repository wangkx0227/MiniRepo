from .app import dashboard_page_bp, dashboard_api, dashboard_api_bp
from .views import workbenches, projects, groups, merge_requests, todos, user_setting, secured_setting
from .api.workbenches import AnnualContributionDataApi, DynamicTimelineDataApi

# page页面
dashboard_page_bp.add_url_rule('/workbenches', view_func=workbenches, methods=['GET'])
dashboard_page_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
dashboard_page_bp.add_url_rule('/groups', view_func=groups, methods=['GET'])
dashboard_page_bp.add_url_rule('/merge_requests', view_func=merge_requests, methods=['GET'])
dashboard_page_bp.add_url_rule('/todos', view_func=todos, methods=['GET'])
dashboard_page_bp.add_url_rule('/setting/user_setting', view_func=user_setting, methods=['GET'])
dashboard_page_bp.add_url_rule('/setting/secured_setting', view_func=secured_setting, methods=['GET'])

# api接口
dashboard_api.add_resource(AnnualContributionDataApi, '/annual_contribution_data')
dashboard_api.add_resource(DynamicTimelineDataApi, '/dynamic_time_line_data')
