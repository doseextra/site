from flask import Flask
from flask_cors import CORS
from dynaconf import settings
from app.core import configuration
from app.utils.helpers import get_absolute_path

static_dir = get_absolute_path(settings.get("STATIC_DIR"))
views_dir = get_absolute_path(settings.get("VIEWS_DIR"))

print(static_dir, views_dir)

def construct(**config):
    app = Flask(__name__, static_folder=static_dir, template_folder=views_dir)
    configuration.init_app(app, **config)
    CORS(app)
    return app


def create_app(**config):
    app = construct(**config)
    configuration.load_extensions(app)
    return app

"""
Create a new app instance.
"""
app = create_app()