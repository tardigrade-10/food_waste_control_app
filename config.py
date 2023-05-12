import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_URI = os.environ.get('MONGODB_URI')
    MONGODB_DB = os.environ.get('MONGODB_DB')

    @staticmethod
    def init_app(app):
        client = MongoClient(Config.MONGODB_URI)
        app.db = client[Config.MONGODB_DB]

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        return app.db


