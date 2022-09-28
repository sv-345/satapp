from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pdf = db.Column(db.String(50000))
    question = db.Column(db.String(50000))
    option1 = db.Column(db.String(10000))
    option2 = db.Column(db.String(10000))
    option3 = db.Column(db.String(10000))
    option4 = db.Column(db.String(10000))
    answer = db.Column(db.Integer)
    iexplanation = db.Column(db.String(50000))
  

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


