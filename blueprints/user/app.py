from flask import Blueprint
from flask_restful import Api

user_page_bp = Blueprint('user_page',
                    __name__,
                    template_folder='templates',  # 指定模板目录，通常是相对于蓝图文件的
                    static_folder='static',  # 指定静态文件目录，通常是相对于蓝图文件的
                    url_prefix='/user'
                    )

user_api_bp = Blueprint('user_api', __name__, url_prefix='/user/api')
user_api = Api(user_api_bp)
