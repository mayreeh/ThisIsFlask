from flask import Flask  
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


from views.home import home
app.register_blueprint(home)

from views.admin import admin
app.register_blueprint(admin)

