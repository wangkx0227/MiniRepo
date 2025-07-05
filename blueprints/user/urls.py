from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting, todos, repos, stars, related

user_page_bp.add_url_rule('/home', view_func=home, methods=['GET']) # 个人主页
user_page_bp.add_url_rule('/setting', view_func=setting, methods=['GET']) # 个人设置
user_page_bp.add_url_rule('/todos', view_func=todos, methods=['GET'])
user_page_bp.add_url_rule('/related', view_func=related, methods=['GET'])
user_page_bp.add_url_rule('/stars', view_func=stars, methods=['GET'])
user_page_bp.add_url_rule('/repos', view_func=repos, methods=['GET'])
