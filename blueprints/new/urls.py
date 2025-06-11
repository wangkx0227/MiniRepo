from .app import new_bp
from .views import projects, organizations, codes

new_bp.add_url_rule('/projects', view_func=projects, methods=['GET'])
new_bp.add_url_rule('/organizations', view_func=organizations, methods=['GET'])
new_bp.add_url_rule('/codes', view_func=codes, methods=['GET'])
