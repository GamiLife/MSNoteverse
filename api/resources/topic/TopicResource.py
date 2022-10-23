from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.helpers.date import DateHelper
from api.pojos.requests.TopicUpdate import TopicUpdate
from api.resources.base.BaseSingleResource import BaseSingleResource
from api.schemas.ResponseSchema import ResponseSchema
from api.services.TopicService import TopicServiceImpl


class TopicResource(Resource):
    base_single_resource = BaseSingleResource("topic", TopicServiceImpl)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Find topic by id',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, topic_id):
        return self.base_single_resource.get(topic_id)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Update topic by id',
                'schema': ResponseSchema
            }
        }
    })
    def put(self, topic_id):
        body = request.get_json(force=True)

        return self.base_single_resource.put(topic_id, body)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Delete topic by id',
                'schema': ResponseSchema
            }
        }
    })
    def delete(self, topic_id):
        now = DateHelper().now().date
        body = {
            "deleted_at": now
        }

        return self.base_single_resource.put(topic_id, body)