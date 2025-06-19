from flask import Blueprint

from .filters import do_date_differ

# 指定的静态和模版相对于蓝图
dashboard_bp = Blueprint('dashboard',
                         __name__,
                         template_folder='templates',
                         static_folder='static',
                         url_prefix='/dashboard'
                         )
# 注册过滤器
dashboard_bp.add_app_template_filter(do_date_differ, "do_date_differ")
