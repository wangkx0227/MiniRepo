from .app import dashboard_bp
from .views import workbenches, projects, groups, merge_requests, todos, user_setting, secured_setting

dashboard_bp.add_url_rule('/workbenches', view_func=workbenches, methods=['GET'])
dashboard_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
dashboard_bp.add_url_rule('/groups', view_func=groups, methods=['GET'])
dashboard_bp.add_url_rule('/merge_requests', view_func=merge_requests, methods=['GET'])
dashboard_bp.add_url_rule('/todos', view_func=todos, methods=['GET'])
dashboard_bp.add_url_rule('/setting/user_setting', view_func=user_setting, methods=['GET'])
dashboard_bp.add_url_rule('/setting/secured_setting', view_func=secured_setting, methods=['GET'])



# 测试假数据接口
# from flask import request, jsonify
#
#
# @dashboard_bp.route('/user/contribution_data')
# def contribution_data():
#     year = int(request.args.get('year', 2025))
#     return jsonify(
#         {'year': year, 'data': {}})
