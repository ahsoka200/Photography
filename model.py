from flask_sqlalchemy import SQLAlchemy
from hello import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    message = db.Column(db.String)

    def __init__(self, username, message):
        self.username = username
        self.message = message



class PhotoInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    place = db.Column(db.String)
    year = db.Column(db.String)
    path = db.Column(db.String)
    category = db.Column(db.String)

    def __init__(self, title, place, year, path, category):
        self.title = title
        self.place = place
        self.year = year
        self.path = path
        self.category = category

