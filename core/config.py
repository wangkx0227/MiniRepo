from datetime import timedelta

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SECRET_KEY = "a_super_random_and_long_secret_key_!@#"
SESSION_TYPE = "redis"  # session存储的类型,
SESSION_PERMANENT = False  # 可选，是否永久 session
SESSION_USE_SIGNER = True  # 对 session id 做签名，提高安全性
SESSION_COOKIE_NAME = "authentication-uid"  # 前端cookie名称
SESSION_COOKIE_HTTPONLY = True  # 前端 JS 不能读取（默认就是 True）"
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)  # session的过期时间


