import json
from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from api.pojos.responses.Response import Response
from api.pojos.responses.TopicWithNotes import TopicWithNotes
from api.schemas.ResponseSchema import ResponseSchema
from api.services.NoteService import NoteService
from api.services.TopicService import TopicService


class TopicWithNotesResource(Resource):
    topic_service_impl = TopicService("topic")
    notes_service_impl = NoteService("notes")

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Get notes by topic id',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, topic_id):
        params = request.args.to_dict()

        try:
            topic_with_notes_info = self.topic_service_impl.find_topic_with_notes_info(topic_id, params)
            notes_by_topic_id = self.notes_service_impl.find_all_by_topic_id(topic_id, params)

            topic_with_notes_response = TopicWithNotes(total_notes=topic_with_notes_info["notes"], total_memorized=topic_with_notes_info["notes_memorized"], notes=notes_by_topic_id)
            topic_with_notes_response_serializable_str = json.dumps(topic_with_notes_response, default=vars)
            topic_with_notes_response_serializable = json.loads(topic_with_notes_response_serializable_str)

            response = Response(data=topic_with_notes_response_serializable, message="%s got successfully!" % "notes")
            return ResponseSchema().dump(response), 200
        except Exception as e:
            print(e)
            response = Response(data=None, message="There was an error")
            return ResponseSchema().dump(response), 500
