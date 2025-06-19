from .app import new_page_bp, new_api
from .views import projects, organizations, codes

new_page_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
new_page_bp.add_url_rule('/organizations', view_func=organizations, methods=['GET'])
new_page_bp.add_url_rule('/codes', view_func=codes, methods=['GET'])
