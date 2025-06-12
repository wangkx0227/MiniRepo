from flask import Blueprint

user_bp = Blueprint('user',
                    __name__,
                    template_folder='templates',  # 指定模板目录，通常是相对于蓝图文件的
                    static_folder='static',  # 指定静态文件目录，通常是相对于蓝图文件的
                    url_prefix='/user'
                    )
