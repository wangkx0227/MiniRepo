from flask import render_template, session, redirect, url_for, request
from resource import redis_link

from .public import get_workbenches_data

"""
    # print(session.get("userStatus")) # 登录使用
    # session["userStatus"] = "asdasdasdwxc312313asdqe"
    # print(redis_link.keys())

"""


# 工作台
def workbenches():
    tab = request.args.get('tab', 'overview')
    # 工作台tab标签，对应get请求参数对应的模版路径
    template_map = {
        'repository': 'dashboard/workbenches/repository.html',
        'analysis': 'dashboard/workbenches/analysis.html',
        'snippet': 'dashboard/workbenches/snippet.html',
        'overview': 'dashboard/workbenches/overview.html'
    }
    # 默认用 overview，无论是登录跳转还是点击工作台
    template = template_map.get(tab, 'dashboard/workbenches/overview.html')
    data_dict = get_workbenches_data(tab)  # 获取当前数据
    # 传递 tab 让前端的tab标签默认选中
    return render_template(template, tab=tab, data=data_dict)


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
