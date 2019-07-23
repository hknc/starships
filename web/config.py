import os


class BaseConfig(object):
    DEBUG = os.environ["DEBUG"]
    DB_NAME = os.environ["POSTGRES_DB"]
    DB_USER = os.environ["POSTGRES_USER"]
    DB_PASS = os.environ["POSTGRES_PASSWORD"]
    DB_SERVICE = os.environ["DB_SERVICE"]
    DB_PORT = os.environ["DB_PORT"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    JSON_SORT_KEYS = False
