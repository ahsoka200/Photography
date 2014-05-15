from hello import db
from flask_sqlalchemy import SQLAlchemy
from model import *

db.create_all()
bob = User('Bob', 'Hello this is Bob')
db.session.add(bob)
db.session.commit()