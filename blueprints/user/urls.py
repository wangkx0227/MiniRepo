from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting, organization, ssh_keys, gpg_keys, private_access_tokens, \
    sessions, repositories, notifications,emails,profile,password,account_information

user_page_bp.add_url_rule('/<username>/home', view_func=home, methods=['GET'])  # 个人主页
user_page_bp.add_url_rule('/setting', view_func=setting, methods=['GET'])  # 个人设置
# 个人设置-组织
user_page_bp.add_url_rule('/setting/organization', view_func=organization, methods=['GET'])
# 个人设置-ssh密钥
user_page_bp.add_url_rule('/setting/ssh_keys', view_func=ssh_keys, methods=['GET'])
# 个人设置-GPG密钥
user_page_bp.add_url_rule('/setting/gpg_keys', view_func=gpg_keys, methods=['GET'])
# 个人设置-私人密钥
user_page_bp.add_url_rule('/setting/private_access_tokens', view_func=private_access_tokens, methods=['GET'])
# 个人设置-活跃会话
user_page_bp.add_url_rule('/setting/sessions', view_func=sessions, methods=['GET'])
# 个人设置-仓库选择
user_page_bp.add_url_rule('/setting/repositories', view_func=repositories, methods=['GET'])
# 个人设置-通知消息
user_page_bp.add_url_rule('/setting/notifications', view_func=notifications, methods=['GET'])
# 个人设置-用户邮箱
user_page_bp.add_url_rule('/setting/emails', view_func=emails, methods=['GET'])
# 个人设置-资料
user_page_bp.add_url_rule('/setting/profile', view_func=profile, methods=['GET'])
# 个人资料-密码
user_page_bp.add_url_rule('/setting/password', view_func=password, methods=['GET'])
# 个人资料-账户资料
user_page_bp.add_url_rule('/setting/account_information', view_func=account_information, methods=['GET'])