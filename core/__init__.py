import os

from config import config_options
from extensions import init_app

from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    # configure app
    ENV = os.getenv('ENV', 'dev')

    app.config.from_object(
        config_options[ENV]
    )

    # configure extensions
    init_app(app)

    # register blueprints
    from core.api import api
    app.register_blueprint(api)

    return app
