from flask import jsonify
from flask_restful import Resource

import traceback
import logging


class BaseResource(Resource):
    """
    项目通用API基类，实现统一响应、异常处理、权限校验、日志等
    """

    def before_auth(self):
        """
        鉴权前置钩子，可重写
        """
        pass

    def auth_check(self):
        """
        鉴权逻辑，可重写（如 JWT、Session 等）
        """
        # if not g.user:
        #     raise PermissionError("未登录")
        pass

    def before_validate(self):
        """
        参数校验前置钩子，可重写
        """
        pass

    def validate_args(self):
        """
        参数校验逻辑，可重写
        """
        pass

    def dispatch_request(self, *args, **kwargs):
        try:
            # 鉴权钩子
            self.before_auth()
            self.auth_check()

            # 参数校验钩子
            self.before_validate()
            self.validate_args()

            # 业务主逻辑
            response = super().dispatch_request(*args, **kwargs)
            print(response)
            # 响应处理钩子
            return self.response_message(response)
        except Exception as e:
            # 异常、日志处理
            logging.error(traceback.format_exc())
            return self.handle_exception(e)

    @staticmethod
    def handle_exception(e):
        """
        统一异常响应和日志
        """
        msg = str(e)
        code = -1
        http_code = 500

        # 可按异常类型自定义
        if isinstance(e, PermissionError):
            code = 401
            http_code = 401
            msg = "权限不足"
        elif isinstance(e, ValueError):
            code = 400
            http_code = 400
            msg = str(e)
        # 其他自定义异常类型...

        return jsonify({
            "code": code,
            "message": msg,
            "data": None
        }), http_code

    @staticmethod
    def response_message(data=None, message="success", code=0):
        """
        统一成功响应消息
        """
        return jsonify({
            "code": code,
            "message": message,
            "data": data
        })
