from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

host = 'localhost'
port = 27017
username = 'vmix-woolf'
password = 'aJLoL1ehSf4qHO0a'
auth_db = 'admin'

def get_db():
    try:
        client = MongoClient(
            host,
            port,
            username=username,
            password=password,
            authSource=auth_db
        )

        print("Підключення до MongoDB успішне!")
        return client["animals"]
    except ConnectionFailure as e:
        print(f"Помилка підключення до MongoDB: {e}")
        exit(1)


db = get_db()
collection = db['cats']