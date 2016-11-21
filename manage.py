
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from app import app, db

#  Development environment
app.config.from_object(os.environ['APP_SETTINGS'])

# Database migrations instance from app and db
migrate = Migrate(app, db)

# Create a Manager instance
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
