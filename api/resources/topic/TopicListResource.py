import json
from http import HTTPStatus

from flasgger import swag_from
from flask import request,jsonify
from flask_restful import Resource

from api.pojos.requests.TopicCreate import TopicCreate
from api.pojos.responses.Response import Response
from api.resources.base.BaseAllResource import BaseAllResource
from api.schemas.ResponseSchema import ResponseSchema
from api.services.TopicService import TopicServiceImpl


class TopicListResource(Resource):
    base_all_resource = BaseAllResource("topics", TopicServiceImpl)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Get topics',
                'schema': ResponseSchema
            }
        }
    })
    def get(self):
        params = request.args.to_dict()

        try:
            list = TopicServiceImpl.find_all_v1(params)

            response = Response(data=list, message="%s got successfully!" % "topics")
            return ResponseSchema().dump(response), 200
        except Exception as e:
            print(e)
            response = Response(data=None, message="There was an error")
            return ResponseSchema().dump(response), 500

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Create a new one topic',
                'schema': ResponseSchema
            }
        }
    })
    def post(self):
        body = request.get_json(force=True)
        body_parse = TopicCreate(body["title"], body["description"], body["user_id"])

        return self.base_all_resource.post(vars(body_parse))
