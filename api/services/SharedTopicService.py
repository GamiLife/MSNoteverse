import json
from datetime import datetime

import pytz
from bson import ObjectId

from api.helpers.date import DateHelper
from api.services.crud import CrudService
from config.extensions import mongo
from config.server_config import server_config


class SharedTopicService(CrudService):
    def __init__(self,collection_name):
        super().__init__(collection_name)

    def find_by_topic_id(self, topic_id: str):
        try:
            document = mongo.db["shared_topics"].find_one({"topic_id": ObjectId(topic_id)})
            json_document = json.loads(json.dumps(document, default=lambda o: str(o)))

            if json_document is None:
                raise Exception("Topic not found!")

            return json_document
        except Exception as error:
            raise Exception(error)

    def create_temporal_shared_topic(self,topic,notes,user):
        date_created = DateHelper().now().date

        try:
            with mongo.db.client.start_session() as session:
                mongo.db["shared_topics"].create_index(keys="create_at",
                                                       expireAfterSeconds=server_config["expiration_time_ttl"],
                                                       session=session)
                document = {
                    "username": user["username"],
                    "topic_title": topic["title"],
                    "topic_id": ObjectId(topic["_id"]),
                    "user_limit": 0,
                    "create_at": date_created,
                    "notes": notes
                }
                mongo.db["shared_topics"].insert_one(document)

                document_response = {
                    "_id": document["_id"],
                    "username": document["username"],
                    "topic_title": document["topic_title"],
                    "topic_id": document["topic_id"],
                    "user_limit": document["user_limit"],
                    "create_at": date_created,
                }

                shared_topic_created_serialized = json.loads(json.dumps(document_response, default=lambda o: str(o)))
                return shared_topic_created_serialized
        except Exception as error:
            print(error)
            raise Exception("Failed on create shared topic with index")


SharedTopicServiceImpl = SharedTopicService("shared_topics")
