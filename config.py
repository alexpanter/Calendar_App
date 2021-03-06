import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #database path
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')         #folder for migrate data files
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"
