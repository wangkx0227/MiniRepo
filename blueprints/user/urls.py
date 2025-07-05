from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting, repository, stars

user_page_bp.add_url_rule('/home', view_func=home, methods=['GET']) # 个人主页
user_page_bp.add_url_rule('/setting', view_func=setting, methods=['GET']) # 个人设置
user_page_bp.add_url_rule('/stars', view_func=stars, methods=['GET']) # 关注
user_page_bp.add_url_rule('/repository', view_func=repository, methods=['GET']) # 仓库



