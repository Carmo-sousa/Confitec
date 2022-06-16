from flask import Flask

from confitec.ext import configuration

app = Flask(__name__)
configuration.init_app(app)


@app.get("/")
def index():
    return "Hello, world!"
