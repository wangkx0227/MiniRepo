from flask import render_template, session


def workbenches():
    # print(session.get("userStatus")) # 登录使用
    session["userStatus"] = "asdasdasdwxc312313asdqe"
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
