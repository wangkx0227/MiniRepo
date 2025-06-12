import redis


class RedisLink:
    __doc__ = "Redis 连接池对象"

    def __init__(self, host, port, db, password=None, max_connections=20, socket_timeout=5):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.max_connections = max_connections
        self.socket_timeout = socket_timeout

    @property
    def pool(self):
        # 创建连接池
        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,  # 没有密码可以省略
            max_connections=self.max_connections,  # 最大连接数，可自定义
            socket_timeout=self.socket_timeout
        )
        return pool



# # # 使用连接池创建 Redis 客户端
#
# r = RedisLink(host="127.0.0.1", port=6379, db=0)
#
# r2 = redis.Redis(connection_pool=r.pool)
# print(r2.ping())
# try:
#     r2.set("key", "value")  # 此时才会尝试连接 Redis 服务器
# except redis.exceptions.ConnectionError as e:
#     print("连接失败：", e)
