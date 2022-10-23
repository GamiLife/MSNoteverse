from bson import ObjectId
from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.get_collection("users").insert_many([
            {
                "_id": ObjectId("631cda65e254720368a68d40"),
                "email": "yei@gmail.com",
                "username": "yei_linux",
                "names": "Yei",
                "firstname": "Linux",
            },
            {
                "_id": ObjectId("631cda65e254720368a68d41"),
                "email": "foo@gmail.com",
                "username": "foobar",
                "names": "Foo",
                "firstname": "Bar",
            }
        ])

    def downgrade(self):
        pass
