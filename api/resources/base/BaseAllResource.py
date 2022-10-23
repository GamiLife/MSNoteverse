from typing import Any

from flask import Request

from api.services.crud import CrudService
from api.pojos.responses.Response import Response
from api.schemas.ResponseSchema import ResponseSchema


class BaseAllResource:
    def __init__(self, resource_name: str, service_impl: CrudService):
        self.resource_name = resource_name
        self.service_impl = service_impl

    def get(self):
        try:
            list = self.service_impl.find_all()

            response = Response(data=list, message="%s got successfully!" % self.resource_name)
            return ResponseSchema().dump(response), 200
        except Exception as e:
            print(e)
            response = Response(data=None, message="There was an error")
            return ResponseSchema().dump(response), 500

    def post(self, data: Any):
        try:
            topic = self.service_impl.create(data)

            response = Response(data=topic, message="%s was created successfully!" % self.resource_name)
            return ResponseSchema().dump(response), 200
        except Exception as e:
            print(e)
            response = Response(data=None, message="There was an error")
            return ResponseSchema().dump(response), 500