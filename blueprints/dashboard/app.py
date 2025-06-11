from flask import Blueprint

# 指定的静态和模版相对于蓝图
dashboard_bp = Blueprint('dashboard',
                         __name__,
                         template_folder='templates',
                         static_folder='static',
                         )