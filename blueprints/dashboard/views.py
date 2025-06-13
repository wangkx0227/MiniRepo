from flask import render_template, session
from resource import redis_link


# 工作台
def workbenches():
    # print(session.get("userStatus")) # 登录使用
    session["userStatus"] = "asdasdasdwxc312313asdqe"
    print(redis_link.keys())
    return render_template("dashboard/workbenches.html")


# 工作台-概览
def workbenches_overview():
    selected = True
    return render_template("dashboard/workbenches/overview.html")


# 工作台-仓库
def workbenches_warehouse():
    selected = True
    return render_template("dashboard/workbenches/warehouse.html")


# 工作台-统计分析
def workbenches_analysis():
    selected = True
    return render_template("dashboard/workbenches/analysis.html")


# 工作台-代码片段
def workbenches_fragment():
    selected = True
    return render_template("dashboard/workbenches/fragment.html")


def projects():
    return render_template("dashboard/projects.html")


def groups():
    return render_template("dashboard/groups.html")


def merge_requests():
    return render_template("dashboard/merge_requests.html")


def todos():
    return render_template("dashboard/todos.html")


def user_setting():
    folded = True  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/user_setting.html", folded=folded)


def secured_setting():
    folded = True  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/secured_setting.html", folded=folded)
