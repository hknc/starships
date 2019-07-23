from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import BaseConfig
from db import db, ma
from resources import StarshipList
from utils import update_starships
from models import Starship

app = Flask(__name__)

#  App config
app.config.from_object(BaseConfig)

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

#  Initialize the database
db.init_app(app)
db.app = app
#  Initialize the Marshmallow
ma.init_app(app)
ma.app = app


def create_tables():
    db.create_all()


#  Initialize the App
@app.before_first_request
def init_app():
    create_tables()
    # Clear old data
    try:
        db.session.query(Starship).delete()
        db.session.commit()
    except:
        db.session.rollback()
    # Collect the starships from SWAPI
    update_starships()


# Setup the Api resource routing
api.add_resource(StarshipList, "/list")

# Register blueprint
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run()
