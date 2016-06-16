from flask_wtf import Form
from wtforms import StringField,SubmitField

class StudentForm(Form):
	firstname = StringField('Firstname')
	lastname = StringField('Lastname')
	SchoolClass = StringField('SchoolClass')
	submit = SubmitField('Add Student')