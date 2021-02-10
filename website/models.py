# where we are storing userdata

# this is importing the variable db from __init__.py
# . is current package
from . import db
from flask_login import UserMixin
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # email is a string with max length of 150
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship("Note")