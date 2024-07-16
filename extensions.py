from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def init_app(app):
    if app:
        db.init_app(app)
        ma.init_app(app)
        migrate.init_app(app, db)
