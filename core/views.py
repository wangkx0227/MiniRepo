from flask import jsonify, render_template, session, redirect, url_for, request


def index():
    """
        首页跳转工作台概览tab
    """
    return redirect(url_for("dashboard_page.workbenches", tab="overview"))


def login():
    """
        登录页
        获取参数,然后登录成功后,跳转到最后访问页面的url

    """
    session["user_status"] = "asdasdasdwxc312313asdqe"  # 默认登录状态
    next_url = request.args.get("get_url")
    if next_url:
        return redirect(next_url)
    return render_template("login.html")


def error_403():
    """
    错误页面403
    page_show_status  用当前值控制侧边栏展示与侧边栏按钮是否可以正常点击
    """
    return render_template("error/403.html", page_show_status=True)


def error_404():
    """
        错误页面404
    """
    return render_template("error/404.html", page_show_status=True)


def health_check():
    """
        健康检查路由
    """
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
