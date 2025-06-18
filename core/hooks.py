import json
from flask import redirect, url_for, session, request

from resource import redis_link
from .variable import FILTER_URL_LIST, URL_REDIS_KEY


def register_hooks(app):
    @app.before_request
    def before():
        """
            作用：
                1.路由验证
                2.路由过滤
                3.登录凭证验证
        """
        url_path = request.path  # 当前访问的路由
        url_method = request.method  # 当前路由访问方法
        endpoint = request.endpoint  # 当前访问路由的视图名称
        filter_url_list = FILTER_URL_LIST
        # 静态文件和无效路由过滤
        if endpoint is None or endpoint == 'static' or endpoint.endswith('.static'):
            return
        # 过滤指定的路由
        if url_path in filter_url_list:
            return
        # 凭证验证
        if not session.get("user_status"):
            original_url = request.full_path  # 原url
            # 如果路由尾部时?说明没有携带get参数,直接分解获取url携带.
            if original_url.endswith("?"):
                original_url = original_url.split("?")[0]
            # 如果用户凭证到期,进行重新登录,携带最后访问的页面url
            return redirect(url_for("login", get_url=original_url))
        # 路由验证
        routes = redis_link.get(URL_REDIS_KEY)
        adapter = app.url_map.bind("localhost")
        _endpoint, _args = adapter.match(url_path, method=url_method)  # 解析的路由参数与路由视图的名称
        if routes:
            routes = json.loads(routes.decode('utf-8'))
        match_status = False
        for i in routes:
            if i.get("endpoint") == _endpoint:
                match_status = True
        if not match_status:
            return redirect(url_for("error_404"))
        print(session.get("user_status"))
        return
