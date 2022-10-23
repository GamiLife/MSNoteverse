from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        validator = {"$jsonSchema": {
            "description": "Users Collection",
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "username": {"type": "string"},
                "names": {"type": "string"},
                "firstname": {"type": "string"},
                "created_at": {"type": "string"},
                "updated_at": {"type": "string"},
                "delete_at": {"type": "string"},
            },
            "required": ["email", "username", "names", "firstname"],
            "dependencies": {}}}

        self.db.create_collection("users", validator=validator)

    def downgrade(self):
        pass
