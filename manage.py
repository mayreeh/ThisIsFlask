import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.models import Students


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

#db.create_all()

if __name__ == '__main__':
    manager.run()