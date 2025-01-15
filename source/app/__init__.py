from source.app.config import Config,db
from flask import Flask
from flask_cors import CORS
import source.app.routes.author_routes

def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app, origins='*',supports_credentials=True)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = Config.url
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS 

    db.init_app(flask_app) 

    flask_app.register_blueprint(source.app.routes.author_routes.author_bp)


    return flask_app
