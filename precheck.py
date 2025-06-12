# 预检功能待完善
import sys
import argparse
from typing import List, Tuple


class PrecheckResult:
    def __init__(self, name: str, passed: bool, message: str = ""):
        self.name = name
        self.passed = passed
        self.message = message

    def __str__(self):
        status = "✅ 通过" if self.passed else "❌ 失败"
        return f"{status} [{self.name}] {self.message}"


def check_python_version() -> PrecheckResult:
    import sys
    min_version = (3, 8)
    if sys.version_info < min_version:
        return PrecheckResult("Python版本", False, f"当前版本为 {sys.version}, 需要 >= 3.8")
    return PrecheckResult("Python版本", True, f"当前版本为 {sys.version}")


def check_requirements() -> PrecheckResult:
    try:
        import pkg_resources
        with open("requirements.txt") as f:
            pkgs = [x.strip() for x in f if x.strip() and not x.startswith("#")]
        pkg_resources.require(pkgs)
        return PrecheckResult("依赖包", True, "全部依赖已安装")
    except Exception as e:
        return PrecheckResult("依赖包", False, f"依赖缺失或版本不符: {e}")


def check_mysql() -> PrecheckResult:
    try:
        from resource.mysql import mysql_link
        mysql_link.ping()
        return PrecheckResult("MySQL", True, "连接成功")
    except Exception as e:
        return PrecheckResult("MySQL", False, f"连接失败: {e}")


def check_redis() -> PrecheckResult:
    try:
        from resource.redis import redis_link
        redis_link.ping()
        return PrecheckResult("Redis", True, "连接成功")
    except Exception as e:
        return PrecheckResult("Redis", False, f"连接失败: {e}")


def check_config_file() -> PrecheckResult:
    import os
    path = "config.json"
    if not os.path.exists(path):
        return PrecheckResult("配置文件", False, f"{path} 不存在")
    try:
        import json
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
        return PrecheckResult("配置文件", True, "配置文件存在且格式正确")
    except Exception as e:
        return PrecheckResult("配置文件", False, f"读取或解析失败: {e}")


def check_dir_permissions() -> PrecheckResult:
    import os
    dirs = ["logs", "uploads"]
    for d in dirs:
        if not os.path.exists(d):
            return PrecheckResult("目录权限", False, f"目录 {d} 不存在")
        if not os.access(d, os.W_OK):
            return PrecheckResult("目录权限", False, f"目录 {d} 无写权限")
    return PrecheckResult("目录权限", True, "所有目录可写")


# 可扩展更多 check_xxx 函数

CHECKS = {
    "python": check_python_version,
    "requirements": check_requirements,
    # "mysql": check_mysql,
    "redis": check_redis,
    "config": check_config_file,
    "dir": check_dir_permissions,
}


def run_checks(selected: List[str] = None) -> List[PrecheckResult]:
    results = []
    checks = CHECKS if selected is None else {k: v for k, v in CHECKS.items() if k in selected}
    for name, func in checks.items():
        res = func()
        print(res)
        results.append(res)
    return results


def main():
    parser = argparse.ArgumentParser(description="项目环境预检")
    parser.add_argument("--only", nargs="*", help="只运行指定检查项，比如: --only mysql redis")
    args = parser.parse_args()
    print(args)
    selected = args.only if args.only else None
    results = run_checks(selected)
    failed = [r for r in results if not r.passed]
    if failed:
        print("\n有检查未通过，启动终止。")
        sys.exit(1)
    print("\n全部检查通过，可以启动项目！")


if __name__ == "__main__":
    main()

"""
    1.端口，文件权限
    2.配置，依赖安装
    3.环境，数据库，缓存
    Python 版本和 pip 版本
    requirements.txt 依赖已安装且版本匹配
    config/config.py 或 .env 文件存在
    MySQL/Postgres 数据库连接正常
    Redis 连接正常
    必要目录可读写（logs/, uploads/, static/ 等）
    检查端口占用
    业务自定义检查（如首次初始化数据）
    
"""
