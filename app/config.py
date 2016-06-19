import os

class Config:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:marystl@localhost/pythonspot'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SECRET_KEY = 's3cr3t'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	csrf_enabled= False
