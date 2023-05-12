from bson.objectid import ObjectId
from app import db

class FoodItem:
    collection = db.food_item

    @classmethod
    def create(cls, item):
        return cls.collection.insert_one(item)

    @classmethod
    def get_all(cls):
        return cls.collection.find()

    @classmethod
    def get_by_id(cls, item_id):
        return cls.collection.find_one({"_id": ObjectId(item_id)})

    @classmethod
    def update(cls, item_id, updates):
        return cls.collection.update_one({"_id": ObjectId(item_id)}, {"$set": updates})

    @classmethod
    def delete(cls, item_id):
        return cls.collection.delete_one({"_id": ObjectId(item_id)})
