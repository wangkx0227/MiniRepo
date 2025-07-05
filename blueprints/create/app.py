from flask import Blueprint
from flask_restful import Api

create_page_bp = Blueprint('create_page',
                        __name__,
                        template_folder='templates',  # 指定模板目录，通常是相对于蓝图文件的
                        static_folder='static',  # 指定静态文件目录，通常是相对于蓝图文件的
                        url_prefix='/c'
                        )

create_api_bp = Blueprint('create_api', __name__, url_prefix='/create/api')
create_api = Api(create_api_bp)
