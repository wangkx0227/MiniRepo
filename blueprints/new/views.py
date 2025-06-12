from flask import render_template


def projects():
    return render_template("new/projects.html")


def organizations():
    return render_template("new/organizations.html")


def codes():
    return render_template("new/codes.html")
