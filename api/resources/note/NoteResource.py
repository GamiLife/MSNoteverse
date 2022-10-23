from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.helpers.date import DateHelper
from api.pojos.requests.NoteUpdate import NoteUpdate
from api.resources.base.BaseSingleResource import BaseSingleResource
from api.schemas.ResponseSchema import ResponseSchema
from api.services.NoteService import NoteServiceImpl


class NoteResource(Resource):
    base_single_resource = BaseSingleResource("note", NoteServiceImpl)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Find note by id',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, note_id):
        return self.base_single_resource.get(note_id)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Update note by id',
                'schema': ResponseSchema
            }
        }
    })
    def put(self, note_id):
        request_body = request.get_json(force=True)

        return self.base_single_resource.put(note_id, request_body)

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Delete note by id',
                'schema': ResponseSchema
            }
        }
    })
    def delete(self, note_id):
        now = DateHelper().now().date
        body = {
            "deleted_at": now
        }

        return self.base_single_resource.put(note_id, body)