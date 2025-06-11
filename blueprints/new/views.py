from flask import render_template


def projects():
    return render_template("projects.html")


def organizations():
    return render_template("organizations.html")


def codes():
    return render_template("codes.html")
