from db import ma
from models import Starship


class StarshipSchema(ma.ModelSchema):
    class Meta:
        model = Starship
        # Fields to expose
        fields = ("name", "hyperdrive")
        ordered = False


starship_schema = StarshipSchema()
starships_schema = StarshipSchema(many=True)


class StarshipUnknownHyperdriveSchema(ma.ModelSchema):
    class Meta:
        model = Starship
        # Fields to expose
        fields = ("name",)


starships_schema = StarshipSchema(many=True)
starships_unknown_hyperdrive_schema = StarshipUnknownHyperdriveSchema(many=True)
