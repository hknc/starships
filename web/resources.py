from flask import jsonify
from flask_restful import Resource

from models import Starship
from schema import starships_schema, starships_unknown_hyperdrive_schema


class StarshipList(Resource):
    def get(self):
        # starships
        starships = Starship.query.filter(Starship.hyperdrive.isnot(None)).order_by(
            Starship.hyperdrive
        )
        starships_list = starships_schema.dump(starships)
        # starships_unknown_hyperdrive
        starships_unknown_hyperdrive = Starship.query.filter(
            Starship.hyperdrive.is_(None)
        )
        starships_unknown_hyperdrive_list = starships_unknown_hyperdrive_schema.dump(
            starships_unknown_hyperdrive
        )
        return jsonify(
            {
                "starships": starships_list.data,
                "starships_unknown_hyperdrive": starships_unknown_hyperdrive_list.data,
            }
        )
