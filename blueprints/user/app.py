from flask import Blueprint
from flask_restful import Api

user_page_bp = Blueprint('user_page',
                         __name__,
                         template_folder='templates',  # 指定模板目录，通常是相对于蓝图文件的
                         static_folder='static',  # 指定静态文件目录，通常是相对于蓝图文件的
                         static_url_path='/u/static'  # 这里指定蓝图静态文件访问路径前缀，防止静态文件找到跟目录下的static文件中
                         )

user_api_bp = Blueprint('user_api', __name__, url_prefix='/u/api')
user_api = Api(user_api_bp)
