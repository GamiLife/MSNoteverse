from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.pojos.requests.SharedTopicCreate import SharedTopicCreate
from api.pojos.responses.Response import Response
from api.schemas.ResponseSchema import ResponseSchema
from api.services.NoteService import NoteService
from api.services.SharedTopicService import SharedTopicService
from api.services.TopicService import TopicService
from api.services.UserService import UserService
from config.server_config import server_config


class SharedTopicListResource(Resource):
    topic_service = TopicService(collection_name="topics")
    note_service = NoteService(collection_name="notes")
    user_service = UserService(collection_name="users")
    shared_topic_service = SharedTopicService(collection_name="shared_topics")

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Create shared topic',
                'schema': ResponseSchema
            }
        }
    })
    def post(self):
        try:
            body = request.get_json(force=True)
            body_parse = SharedTopicCreate(topic_id=body["topic_id"],user_id=body["user_id"])

            topic = self.topic_service.find_by_id(body_parse.topic_id)

            if topic is None:
                raise Exception("Topic not found")

            user = self.user_service.find_by_id(topic["user_id"])

            if body_parse.user_id != topic["user_id"]:
                raise Exception("Incorrect user id")

            filters_dict = {"size": 15,"page": 0,"sort_by": "title"}
            notes = self.note_service.find_all_by_topic_id(body_parse.topic_id,filters_dict)
            shared_topic_created = self.shared_topic_service.create_temporal_shared_topic(topic,notes,user)

            response = Response(data=shared_topic_created,
                                message="Was created successful, remember that this shared topic created will expire in %s seconds" %
                                        server_config["expiration_time_ttl"])
            return ResponseSchema().dump(response),200
        except Exception as error:
            response = Response(data=None,message="Error found: %s" % error)
            return ResponseSchema().dump(response),500
