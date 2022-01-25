from app.http.controllers import blog_controller
from flask import Blueprint

blog = Blueprint("blog", __name__, url_prefix="/blog")


@blog.route("/", methods=["GET"])
def index():
    return blog_controller.index()


def init_app(app):
    app.register_blueprint(blog)
