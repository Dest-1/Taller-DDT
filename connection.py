from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["Taller_DTT"]

    collection_name = "test"
    collection = database[collection_name]

    return collection