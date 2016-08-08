from app import db

from flask import url_for
from flask_admin import form
from flask_admin.form import rules
from flask_admin.contrib import sqla


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(32))
    description = db.Column(db.Text)
    
    start = db.Column(db.DateTime)
    stop = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<Task %r>' % self.title
