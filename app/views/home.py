from flask import Blueprint
from .. import app

home = Blueprint('home' , __name__)

@home.route('/home')
def home():
	return "This is home page"


