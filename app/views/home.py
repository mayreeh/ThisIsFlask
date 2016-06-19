from flask import Blueprint , render_template , request
from .. import app , db
from ..studform import StudentForm
from ..models import Students
app.secret_key = 's3cr3t'

home = Blueprint('home' , __name__)

@home.route('/home' , methods = ('POST' , 'GET'))
def index():
	form = StudentForm()
	stud = {}
	if request.method == 'GET':
		return render_template('homeindex.html' , form = form)
	else:
		form = StudentForm(request.form)
		form_studs = Students()
        form.populate_obj(form_studs)
        db.session.add(form_studs)
        db.session.commit()
		



