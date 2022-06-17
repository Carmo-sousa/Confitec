from importlib import import_module

from dynaconf import FlaskDynaconf

from confitec.ext import database


def load_extensions(app):
    for extension in app.config.get("EXTENSIONS"):
        mod = import_module(extension)
        mod.init_app(app)
    database.init_app()


def init_app(app):
    FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"])
    return app
