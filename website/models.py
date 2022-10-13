from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    
class Log4(db.Model):
    
   id = db.Column('id', db.Integer, primary_key = True)
   password = db.Column(db.String(100))
   email = db.Column(db.String(50))
   base_url = db.Column(db.String(200)) 
   host = db.Column(db.String(100))    
   method=db.Column(db.String(100))
   processed=db.Column(db.String(100))
   TimeProcess=db.Column(db.String(100))
   Status=db.Column(db.Boolean)


    
