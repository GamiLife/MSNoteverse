import json
import re

from bson import json_util,ObjectId

from api.services.crud import CrudService
from config.extensions import mongo


class NoteService(CrudService):
    def __init__(self, collection_name):
        super().__init__(collection_name)

    def find_all_by_topic_id(self, topic_id: str, filters_pagination):
        try:
            skip = int(filters_pagination["size"]) * int(filters_pagination["page"])
            regx = re.compile(filters_pagination["search"], re.IGNORECASE)

            like = None if filters_pagination["is_liked"] is None else None if filters_pagination["is_liked"] == "true" else False
            ignored = None if filters_pagination["is_ignored"] is None else None if filters_pagination["is_ignored"] == "true" else False

            filters = {
               "topic_id": ObjectId(topic_id),
               "deleted_at": None,
               "is_liked": like,
               "is_ignored": ignored
            }

            responses = mongo.db["notes"].aggregate(
                [
                    {
                        "$match": filters
                    },
                    {
                        "$addFields": {
                            "is_match": {
                                "$regexMatch": {
                                    "input": "$title",
                                    "regex": regx,
                                },
                            }
                        }
                    },
                    {
                        "$match": {
                            "is_match": True
                        }
                    },
                    {
                        "$skip": skip
                    },
                    {
                        "$limit":  15
                    },
                    {
                        "$project": {
                            "_id":  1,
                            "title": 1,
                            "description": 1,
                            "is_liked": 1,
                            "is_memorized": 1,
                            "is_ignored": 1,
                            "topic_id": 1
                        }
                    }
                ]
            )

            list_responses = list(responses)
            json_list_responses = list(map(lambda document: json.loads(json.dumps(document, default=lambda o: str(o))), list_responses))

            return json_list_responses
        except Exception as e:
            print(e)
            raise Exception("Error in find all by topic id")


NoteServiceImpl = NoteService("notes")
