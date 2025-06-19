# 成功状态码
SUCCESS = 0  # 请求成功
CREATED = 1001  # 请求的数据已成功创建。
UPDATED = 1002  # 请求的数据已成功更新。
DELETED = 1003  # 请求的数据已成功删除。

# 客户端错误状态码
CLIENT_ERROR = 2000  # 客户端请求有语法错误，服务器无法理解。
MISSING_PARAM = 4000  # 请求缺少必要的参数。
INVALID_PARAM = 4001  # 提供的参数格式不正确。
INVALID_INPUT = 4002  # 用户输入的数据有误。
RESOURCE_NOT_FOUND = 4003  # 用户请求的资源不存在。
PERMISSION_DENIED = 4004  # 用户没有权限访问该资源。

# 授权和认证相关状态码
UNAUTHORIZED = 3000  # 用户未授权，缺少有效的认证信息。
SESSION_EXPIRED = 3001  # 用户会话已过期，需要重新登录。
INSUFFICIENT_PERMISSIONS = 3002  # 用户没有足够的权限执行该操作。
AUTHENTICATION_FAILED = 3003  # 用户认证失败，用户名或密码错误。

# 服务器错误状态码
SERVER_ERROR = 4000  # 服务器内部错误，无法完成请求。
UNEXPECTED_CONDITION = 5000  # 服务器遇到意外情况，无法完成请求。
OVERLOADED = 5001  # 服务器暂时过载或维护，无法处理请求。

# 业务逻辑相关状态码
BUSINESS_RULE_VIOLATION = 6000  # 请求的操作被业务逻辑禁止。

# 数据相关状态码
DATA_VALIDATION_FAILED = 7000  # 请求的数据验证失败。
INCOMPLETE_DATA = 7001  # 请求的数据不完整，缺少必要的字段。
DATA_CONFLICT = 7002  # 请求的数据与现有数据冲突。
