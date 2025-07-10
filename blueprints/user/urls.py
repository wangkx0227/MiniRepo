from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting,  organization, notifications

user_page_bp.add_url_rule('/<username>/home', view_func=home, methods=['GET'])  # 个人主页
user_page_bp.add_url_rule('/<username>/setting', view_func=setting, methods=['GET'])  # 个人设置
user_page_bp.add_url_rule('/<username>/organization', view_func=organization, methods=['GET'])  # 组织
user_page_bp.add_url_rule('/<username>/notifications', view_func=notifications, methods=['GET'])  # 消息通知
