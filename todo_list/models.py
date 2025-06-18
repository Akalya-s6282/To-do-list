from .db import db
#from . import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20), unique=False, nullable=False)
    status = db.Column(db.String(20), unique=False, nullable=False)
