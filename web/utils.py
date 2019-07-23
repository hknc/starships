from db import db
from models import Starship
from services import retrieve_starships


def save_ships(ships):
    ships_to_save = []
    for ship in ships:
        hyperdrive = ship.get("hyperdrive_rating")
        if hyperdrive == "unknown":
            hyperdrive = None
        new_ship = Starship(name=ship.get("name"), hyperdrive=hyperdrive)
        ships_to_save.append(new_ship)

    db.session.bulk_save_objects(ships_to_save)
    db.session.commit()


def update_starships(url="https://swapi.co/api/starships/"):
    api_result = retrieve_starships(url)
    ships, next_page = api_result
    if ships:
        save_ships(ships)
        if next_page:
            update_starships(next_page)
        return True
    return False
