from unicodedata import name
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///LogAll.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
    
   id = db.Column('id', db.Integer, primary_key = True)
   Username = db.Column(db.String(100))
   email = db.Column(db.String(50))
   hostName = db.Column(db.String(200)) 
   addr = db.Column(db.String(100))



student2 = students.query.all()
student3 = students(name="d",city="da",addr="da",pin="da")

db.session.add(student3)
db.session.commit()

db.create_all()
