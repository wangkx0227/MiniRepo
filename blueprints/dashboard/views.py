from flask import render_template, session, redirect, url_for, request
# from utils import redis_link

from .views_data import get_workbenches_data

"""
    # print(session.get("userStatus")) # 登录使用
    # session["userStatus"] = "asdasdasdwxc312313asdqe"
    # print(redis_link.keys())

"""


# 工作台
def workbenches():
    return render_template("dashboard/workbenches.html")


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
