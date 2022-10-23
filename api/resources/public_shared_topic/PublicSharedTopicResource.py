from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.pojos.requests.SharedTopicCreate import SharedTopicCreate
from api.pojos.responses.Response import Response
from api.resources.base.BaseSingleResource import BaseSingleResource
from api.schemas.ResponseSchema import ResponseSchema
from api.services.NoteService import NoteService
from api.services.SharedTopicService import SharedTopicService,SharedTopicServiceImpl
from api.services.TopicService import TopicService
from api.services.UserService import UserService
from config.server_config import server_config


class PublicSharedTopicResource(Resource):
    shared_topic_service = SharedTopicService(collection_name="shared_topics")

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Get public shared topic by shared topic id',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, shared_topic_id):
        try:
            shared_topic = self.shared_topic_service.find_by_id(shared_topic_id)

            if shared_topic is None:
                raise Exception("Shared topic was not found.")

            response = Response(data=shared_topic,
                                message="Got data successful, remember that this shared topic created will expire in %s seconds" %
                                        server_config["expiration_time_ttl"])
            return ResponseSchema().dump(response),200
        except Exception as error:
            response = Response(data=None,message="Error found: %s" % error)
            return ResponseSchema().dump(response),500
