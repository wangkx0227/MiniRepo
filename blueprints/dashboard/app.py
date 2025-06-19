from flask import Blueprint
from flask_restful import Api
from .filters import do_date_differ

# 指定的静态和模版相对于蓝图
dashboard_page_bp = Blueprint('dashboard_page',
                              __name__,
                              template_folder='templates',
                              static_folder='static',
                              url_prefix='/dashboard'
                              )
# 注册过滤器
dashboard_page_bp.add_app_template_filter(do_date_differ, "do_date_differ")
# 注册 api
dashboard_api_bp = Blueprint('dashboard_api', __name__, url_prefix='/dashboard/api')
dashboard_api = Api(dashboard_api_bp)
