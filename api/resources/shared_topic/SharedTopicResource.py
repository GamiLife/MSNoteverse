from http import HTTPStatus

from flasgger import swag_from
from flask_restful import Resource

from api.helpers.date import DateHelper
from api.pojos.responses.Response import Response
from api.schemas.ResponseSchema import ResponseSchema
from api.services.SharedTopicService import SharedTopicService
from config.server_config import server_config


class SharedTopicResource(Resource):
    shared_topic_service = SharedTopicService(collection_name="shared_topics")

    @swag_from({
        'responses': {
            HTTPStatus.OK.value: {
                'description': 'Get shared topic inside of app with topic id(authenticated)',
                'schema': ResponseSchema
            }
        }
    })
    def get(self, topic_id):
        try:
            shared_topic = self.shared_topic_service.find_by_topic_id(topic_id)

            if shared_topic is None:
                raise Exception("Shared topic was not found.")

            now = DateHelper().now().date
            date_created = DateHelper(date=shared_topic["create_at"]).add(seconds=server_config["expiration_time_ttl"]).tz().diff(now)

            shared_topic["create_at"] = DateHelper(date=shared_topic["create_at"]).tz().str()

            if date_created["invalid"] is True:
                response = Response(data={**shared_topic, "warning": "Shared topic it will expired soon!."},
                                    message="Got data successful, remember that this shared topic created will expire be expired")
                return ResponseSchema().dump(response),200

            field_dict = None

            if date_created["dd"] > 0:
                field_dict = {"short": "dd", "long": "day(s)"}
            if field_dict is None and date_created["mm"] > 0:
                field_dict = {"short": "mm", "long": "minute(s)"}
            if field_dict is None:
                field_dict = {"short": "ss", "long": "second(s)"}

            warning_message = "This shared topic with your notes going to be expired in %s %s" % (date_created[field_dict["short"]], field_dict["long"])

            response = Response(data={**shared_topic, "warning": warning_message},
                                message="Got data successful, remember that this shared topic created will expire be expired")
            return ResponseSchema().dump(response),200
        except Exception as error:
            response = Response(data=None,message="Error found: %s" % error)
            return ResponseSchema().dump(response),500
