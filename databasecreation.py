from hello import db
from flask_sqlalchemy import SQLAlchemy
from model import *

db.drop_all()
db.create_all()
bob = User('Bob', 'Hello this is Bob')
db.session.add(bob)
db.session.commit()

image_one = PhotoInfo('splash', 'Los Altos', '2013', '/action/IMG_9696.jpg')
