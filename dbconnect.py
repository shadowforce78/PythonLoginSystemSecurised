from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def get_database():
    uri = "mongodb+srv://scriptorjs:adam1903@arceusjs.aarhd.mongodb.net/pythongame"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi("1"))

    # Create the db object
    db = client.pythongame

    return db
