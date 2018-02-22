# flask/app/__init__.py

# This file initializes the flask app, the database,
# and the admin panel.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# instantiating Flask-app
app = Flask(__name__, static_folder='static')


# using the config file to.. ??
# app.config.from_object("config")
app.secret_key = "something"
app.config.from_object('config')


# instantiating SQLAlchemy as our database
db = SQLAlchemy(app)


# creating the admin panel
admin = Admin(app, name='admin page', template_mode="bootstrap3")


from app import views, models
from models import Task

# attaching model views to the admin panel from the db classes
admin.add_view(ModelView(Task, db.session))

