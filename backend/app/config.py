import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/app-dev.db"
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://homestead:secret@localhost:3306/homestead'


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "I'm Ron Burgundy?")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/app-dev.db"
    # msqldb_uri = 'mysql+pymysql://root:password@localhost:3309/sqlalchemy'
    # msqldb_uri = 'mysql+pymysql://root:password@localhost:3306/sqlalchemy'
    msqldb_uri = 'mysql+pymysql://homestead:secret@db:3306/homestead'



EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}