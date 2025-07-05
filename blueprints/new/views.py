from flask import render_template


def projects():
    return render_template("n_projects.html")


def groups():
    return render_template("n_groups.html")


def snippets():
    return render_template("n_snippets.html")
