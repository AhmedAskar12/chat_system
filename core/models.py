from datetime import date
from flask_login import UserMixin

from core import db 


class User(db.Model, UserMixin):
    __tablename__= "Users"

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=False)
    created = db.Column(db.Date, default=date.today())
    agent = db.Column(db.Boolean, default=False)
