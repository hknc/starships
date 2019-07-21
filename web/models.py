from db import db


class Starship(db.Model):

    __tablename__ = "starships"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    hyperdrive = db.Column(db.Numeric(10, 2), nullable=True)

    def __init__(self, name, hyperdrive):
        self.name = name
        self.hyperdrive = hyperdrive

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
