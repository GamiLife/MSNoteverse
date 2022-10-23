from bson import ObjectId
from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        validator = {"$jsonSchema": {
            "description": "Notes Collection",
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "is_liked": {"type": "boolean"},
                "created_at": {"type": "string"},
                "updated_at": {"type": "string"},
                "delete_at": {"type": "string"},

                "topic_id": {"bsonType": "objectId"},

                "is_memorized": {"type": "boolean"},
                "is_ignored": {"type": "boolean"}
            },
            "required": ["title", "description", "topic_id"],
            "dependencies": {}}}

        self.db.create_collection("notes", validator=validator)

    def downgrade(self):
        pass
