from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.create_collection("sessions")

    def downgrade(self):
        pass
