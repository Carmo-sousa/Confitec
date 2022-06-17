from flask import Flask

from .artists import bp as module


def init_app(app: Flask):
    app.register_blueprint(module)
