from flask import render_template


def workbenches():
    return render_template("dashboard/workbenches.html")


def projects():
    return render_template("dashboard/projects.html")


def groups():
    return render_template("dashboard/groups.html")


def merge_requests():
    return render_template("dashboard/merge_requests.html")


def todos():
    print(2131312)
    return render_template("dashboard/todos.html")


def user_setting():
    folded = "interfaceSidebarSetting"  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/user_setting.html", folded=folded)


def secured_setting():
    folded = "interfaceSidebarSetting"  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/secured_setting.html", folded=folded)
