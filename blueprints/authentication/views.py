from flask import render_template


def home():
    return render_template("home.html")


def setting():
    return render_template("setting.html")


def todos():
    return render_template("todos.html")


def related():
    return render_template("related.html")


def stars():
    return render_template("stars.html")


def repos():
    return render_template("repos.html")
