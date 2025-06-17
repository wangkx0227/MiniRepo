import json
from resource import redis_link
from .filters import do_date_differ


def save_routes_to_redis(f_app):
    """
        存储项目全部url到redis
    """
    routes = []
    for rule in f_app.url_map.iter_rules():
        if rule.endpoint == 'static' or rule.endpoint.endswith('.static'):  # 过滤静态路由
            continue
        routes.append({
            "rule": rule.rule,
            "endpoint": rule.endpoint,
            "methods": list(rule.methods)
        })
    # 保存为 JSON 字符串
    redis_link.set(f_app.config["URL_REDIS_KEY"], json.dumps(routes, ensure_ascii=False))


def register_filters(f_app):
    f_app.add_template_filter(do_date_differ, "do_date_differ")
