from flask import Blueprint
from flask_restful import Api

new_page_bp = Blueprint('new_page',
                        __name__,
                        template_folder='templates',  # 指定模板目录，通常是相对于蓝图文件的
                        static_folder='static',  # 指定静态文件目录，通常是相对于蓝图文件的
                        url_prefix='/new'
                        )

new_api_bp = Blueprint('new_api', __name__, url_prefix='/n/api')
new_api = Api(new_api_bp)
