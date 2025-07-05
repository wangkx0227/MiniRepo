# 全部的自定义过滤器全部在这个文件
from datetime import datetime


# 过滤器 - 计算当前提交代码的更新时间
def do_date_differ(p_data):
    old_time = datetime.strptime(p_data, "%Y-%m-%d %H:%M:%S")
    current_time = datetime.now()
    differ = current_time - old_time
    seconds = differ.total_seconds() # 秒
    diff_minutes = int(seconds // 60)  # 分钟
    diff_hours = int(diff_minutes // 60)  # 小时
    diff_days = int(diff_hours // 24)  # 天
    diff_months = int(diff_days // 30)  # 月
    if seconds < 60:
        return "刚刚"
    elif diff_minutes < 60:
        return f"{diff_minutes}分钟前"
    elif diff_hours < 24:
        return f"{diff_hours}小时前"
    elif diff_days < 7:
        return f"{diff_days}天前"
    elif diff_months < 365:
        return f"{diff_months}个月前"
    return "超过1年前"
