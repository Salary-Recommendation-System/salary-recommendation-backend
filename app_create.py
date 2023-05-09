from flask import Flask
from flask_cors import CORS

from Controller.Controller import bp
from Resources.Config import Config
from Resources.Database import db


def create_app():
    app = Flask(__name__)
    CORS(app)

    config = Config()
    build_uri = f"postgresql://{config.get('user')}:{config.get('password')}@{config.get('host')}/{config.get('name')}"

    app.config['SQLALCHEMY_DATABASE_URI'] = build_uri
    db.init_app(app)
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
    return app
