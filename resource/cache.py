
import redis
from .config import cache_conf_dict


class RedisLink:
    """Redis 连接池对象"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, port, db, password=None, max_connections=20, socket_timeout=5):
        self._pool = redis.ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=max_connections,
            socket_timeout=socket_timeout,
            decode_responses=False
        )
        self._redis = redis.Redis(connection_pool=self._pool)

    @property
    def redis_link_object(self):
        return self._redis


cache_config = cache_conf_dict

r = RedisLink(host=cache_config.get("host"), port=cache_config.get("port"), db=cache_config.get("db"),
              password=cache_config.get("password"), max_connections=cache_config.get("max_connections"),
              socket_timeout=cache_config.get("socket_timeout"))
redis_link = r.redis_link_object
