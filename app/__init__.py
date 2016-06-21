from flask import Flask  
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from config import Config
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

db.create_all()

from views.home import home
app.register_blueprint(home)

from views.admin import admin
app.register_blueprint(admin)

