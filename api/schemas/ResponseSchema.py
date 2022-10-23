from typing import Any

from flask_marshmallow import Schema
from marshmallow.fields import Str, Raw


class ResponseSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["data", "message"]

    data = Raw()
    message = Str()
