from flask import Flask  
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)


from views.home import home
app.register_blueprint(home)

from views.admin import admin
app.register_blueprint(admin)

