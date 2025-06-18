from flask import jsonify, render_template, session, redirect, url_for, request


# 错误页面403
def error_403():
    # page_show_status  用当前值控制侧边栏展示与侧边栏按钮是否可以正常点击
    return render_template("error/403.html", page_show_status=True)


# 错误页面404
def error_404():
    return render_template("error/404.html", page_show_status=True)


# 首页
def index():
    return redirect(url_for("dashboard.workbenches", tab="overview"))


# 登录页
def login():
    # 获取参数,然后登录成功后,跳转到最后访问页面的url
    session["user_status"] = "asdasdasdwxc312313asdqe"  # 默认登录状态
    next_url = request.args.get("get_url")
    if next_url:
        return redirect(next_url)
    return render_template("login.html")


# 健康检查路由
def health_check():
    """健康检查"""
    checks = {
        "ProjectStatus": True,
        "Resource": {
            "MySQL": {
                "Version": "5.7.31",
                "Status": True,
                "Message": ""
            },
            "Redis": {
                "Version": "5.0.14.1",
                "Status": True,
                "Message": "",
            },
        }
    }
    status = 200
    return jsonify(checks), status
