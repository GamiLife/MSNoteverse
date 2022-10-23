import argparse

from mongodb_migrations.cli import MigrationManager

"""
Migrations Manager, to execute scripts run:
    * create migration: py migration_manager.py --type create --name file_name
    * run migration :   py migration_manager.py --type run
"""


def init():
    parser = argparse.ArgumentParser(description="Custom MondoDB Migration parser")
    parser.add_argument('--type',help="Process type: 'create' | 'run'")
    parser.add_argument('--name',help="Name in migration title")

    args = parser.parse_args()

    migration_name = args.name
    migration_type = args.type

    if migration_type != 'create' and migration_type != 'run':
        raise Exception("Please, you should pass create or run value.")

    if migration_type == 'create' and migration_name is None:
        raise Exception("Please, you should pass migration name parameter.")

    manager = MigrationManager()
    manager.config.config_file = "config.ini"

    if migration_type == 'run':
        manager.run()
        return

    manager.config.description = migration_name

    manager.create_migration()


if __name__ == '__main__':
    init()
