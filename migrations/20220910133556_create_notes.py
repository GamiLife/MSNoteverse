from bson import ObjectId
from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.get_collection("notes").insert_many([
            {
                "_id": ObjectId("631cdc817bf8d43c89e80d10"),
                "title": "Julio Cesar",
                "description": "Julio Cesar and Cleopatra worked together and then they had a son",
                "is_liked": False,
                "topic_id": ObjectId("631cdb1b250a87dd50fb5080"),

                "is_memorized": True,
                "is_ignored": False
            },
            {
                "_id": ObjectId("631cdc817bf8d43c89e80d11"),
                "title": "Synesthesia",
                "description": "Faculty not common whose some people experiments strange sensations",
                "is_liked": True,
                "topic_id": ObjectId("631cdb1b250a87dd50fb5081"),

                "is_memorized": False,
                "is_ignored": False
            },
            {
                "_id": ObjectId("631cdc817bf8d43c89e80d12"),
                "title": "Hash Map",
                "description": "Data structure that offers a good tradeoff between time and space costs",
                "is_liked": True,
                "topic_id": ObjectId("631cdb1b250a87dd50fb5082"),

                "is_memorized": False,
                "is_ignored": False
            },
        ])

    def downgrade(self):
        pass
