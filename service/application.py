from flask import Flask

from .settings import get_config


def create_application():
    config = get_config()
    app = Flask(__name__)
    app.config.from_object(config)
    return app
