URL_REDIS_KEY = "url_all_list"  # 存储项目下全部url到redis的key
FILTER_URL_LIST = ["/login", "/error/403", "/error/404", "/health_check"]  # 过滤url,不会被验证,直接放行
