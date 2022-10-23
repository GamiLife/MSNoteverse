import json
from typing import Dict

import jsonpatch
from bson import json_util,ObjectId

from config.extensions import mongo


class CrudService:
    _collection_name: str

    def __init__(self,collection_name):
        self._collection_name = collection_name

    def find_all(self):
        try:
            print("test")
            print(mongo.db[self._collection_name])
            responses = mongo.db[self._collection_name].find({})
            list_responses = list(responses)
            json_list_responses = list(map(lambda document: json.loads(json.dumps(document, default=lambda o: str(o))), list_responses))

            return json_list_responses
        except Exception as e:
            raise Exception("Error in find all: ", e)

    def find_by_id(self, id_param: str):
        try:
            response = mongo.db[self._collection_name].find_one({"_id": ObjectId(id_param)})
            json_document = json.loads(json.dumps(response, default=lambda o: str(o)))
            return json_document
        except Exception as e:
            raise Exception("Error in find by id", e)

    def create(self, document: Dict):
        try:
            mongo.db[self._collection_name].insert_one(document)
            json_document = json.loads(json.dumps(document, default=lambda o: str(o)))

            return json_document
        except Exception as e:
            raise Exception("Error in creating document", e)

    def update_by_id(self, id_param: str, document: Dict):
        try:
            mongo.db[self._collection_name].update_one({"_id": ObjectId(id_param)} , {"$set": document})
            json_document = json.loads(json.dumps(document, default=lambda o: str(o)))
            return json_document
        except Exception as e:
            raise Exception("Error in updating document", e)

    def delete_by_id(self, id_param: str):
        try:
            mongo.db[self._collection_name].delete_one({"_id": ObjectId(id_param)})
        except Exception as e:
            raise Exception("Error in deleting document", e)
