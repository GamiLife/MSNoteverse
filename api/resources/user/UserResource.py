from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.resources.base.BaseSingleResource import BaseSingleResource
from api.schemas.ResponseSchema import ResponseSchema
from api.services.TopicService import TopicServiceImpl


class UserResource(Resource):
    base_single_resource = BaseSingleResource("user", TopicServiceImpl)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Find user by id',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, user_id):
        return self.base_single_resource.get(user_id)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Update user by id',
                'schema': ResponseSchema
            }
        }
    })
    def put(self, user_id):
        return self.base_single_resource.put(user_id, request.get_json())

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Delete users by id',
                'schema': ResponseSchema
            }
        }
    })
    def delete(self, user_id):
        return self.base_single_resource.delete(user_id)