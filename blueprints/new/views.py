from flask import render_template


def projects():
    return render_template("c_projects.html")


def groups():
    return render_template("c_groups.html")


def snippets():
    return render_template("c_snippets.html")
