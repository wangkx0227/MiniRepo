from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting, repository, stars, organization

user_page_bp.add_url_rule('/<username>/home', view_func=home, methods=['GET'])  # 个人主页
user_page_bp.add_url_rule('/<username>/setting', view_func=setting, methods=['GET'])  # 个人设置
user_page_bp.add_url_rule('/<username>/stars', view_func=stars, methods=['GET'])  # 收藏项目
user_page_bp.add_url_rule('/<username>/repository', view_func=repository, methods=['GET'])  # 仓库
user_page_bp.add_url_rule('/<username>/organization', view_func=organization, methods=['GET'])  # 仓库
