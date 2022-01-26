from flask import render_template


def index():
    return render_template("blog/index.html")
