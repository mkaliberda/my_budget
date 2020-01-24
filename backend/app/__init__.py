from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint, abort

db = SQLAlchemy()



def create_app(env=None):
    from .config import config_by_name
    from .routers import register_routes_api_v1

    app = Flask(__name__)
    app.config.from_object(config_by_name[env])
    app.config['OPENAPI_VERSION'] = '3.0.2'
    api = Api(app)
    # regitster api routers
    register_routes_api_v1(api)

    db.init_app(app)

    return app