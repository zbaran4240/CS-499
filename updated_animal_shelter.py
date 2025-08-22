from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

# Class definition of animal shelter object
class AnimalShelter(object):

    # Constructor
    def __init__(self, username, password):
        this.client = MongoClient('mongodb://%s:%s@localhost:32554/AAC' % ("aacuser", "Fr4nk13"))
        self.database = self.client["AAC"]


    # Method which is used to insert a document into animals collection
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
            for document in data:
                print(document)

            else:
                data = self.database.animals.find({}, {"_id": False})

            return data

    # Create method to implement the U in CRUD.
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit=1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")

    # Create method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit=1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")