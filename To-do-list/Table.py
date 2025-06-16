
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20), unique=False, nullable=False)
    status = db.Column(db.String(20), unique=False, nullable=False)
