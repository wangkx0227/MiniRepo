from .app import user_page_bp, user_api_bp, user_api
from .views import home, setting, organization, ssh_keys, gpg_keys, private_access_tokens, \
    conversation_info, repositories, notifications

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
user_page_bp.add_url_rule('/setting/conversation_info', view_func=conversation_info, methods=['GET'])
# 个人设置-仓库
user_page_bp.add_url_rule('/setting/repositories', view_func=repositories, methods=['GET'])
# 个人设置-通知消息
user_page_bp.add_url_rule('/setting/notifications', view_func=notifications, methods=['GET'])
