from app.http.controllers import teste_controller
from flask import Blueprint

teste = Blueprint("teste", __name__, url_prefix="/testes")


@teste.route("/", methods=["GET"])
def index():
    return teste_controller.index()


def init_app(app):
    app.register_blueprint(teste)
