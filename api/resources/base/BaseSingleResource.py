from typing import Any,Dict

from api.services.crud import CrudService
from api.pojos.responses.Response import Response
from api.schemas.ResponseSchema import ResponseSchema


class BaseSingleResource:
    def __init__(self,resource_name: str,service_impl: CrudService):
        self.resource_name = resource_name
        self.service_impl = service_impl

    def get(self, resource_id: str):
        try:
            topic = self.service_impl.find_by_id(resource_id)
            message = "%s got successfully!" % self.resource_name if topic is not None else "There is not %s with this id" % self.resource_name

            response = Response(data=topic,message=message)
            return ResponseSchema().dump(response),200
        except Exception as e:
            print(e)
            response = Response(data=None,message="There was an error")
            return ResponseSchema().dump(response),500

    def put(self, resource_id: str, data: Any):
        try:
            topic = self.service_impl.update_by_id(resource_id,data)
            message = "%s was updated successfully!" % self.resource_name

            response = Response(data=topic,message=message)
            return ResponseSchema().dump(response),200
        except Exception as e:
            print(e)
            response = Response(data=None,message="There was an error")
            return ResponseSchema().dump(response),500

    def delete(self, resource_id: str):
        try:
            topic = self.service_impl.delete_by_id(resource_id)
            message = "%s was deleted successfully!" % self.resource_name

            response = Response(data=topic,message=message)
            return ResponseSchema().dump(response),200
        except Exception as e:
            print(e)
            response = Response(data=None,message="There was an error")
            return ResponseSchema().dump(response),500
