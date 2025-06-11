from flask import render_template


def home():
    return render_template("user/home.html")


def setting():
    return render_template("user/setting.html")


def todos():
    return render_template("user/todos.html")


def related():
    return render_template("user/related.html")


def stars():
    return render_template("user/stars.html")


def repos():
    return render_template("user/repos.html")
