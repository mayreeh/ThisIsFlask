from . import app , db

class Students(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(200))
	lastname = db.Column(db.String(200))
	schoolclass = db.Column(db.String(30))

	def __int__(self,firstname,lastname,schoolclass):
		self.firstname = firstname
		self.lastname = lastname
		self.schoolclass = schoolclass