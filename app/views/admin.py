from flask import Blueprint

admin = Blueprint('admin' , __name__)

@admin.route('/admin')
def index():
	return "This is admin home"