import os
from dotenv import load_dotenv


load_dotenv()  # allows access to env variables


class Base:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Base):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    DEBUG = True


class Staging(Base):
    pass


class TestConfig(Base):
    pass


config_options = {
    'default': DevConfig,
    'dev': DevConfig,
    'testing': TestConfig
}
