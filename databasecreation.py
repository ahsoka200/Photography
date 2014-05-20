dfrom hello import db
from flask_sqlalchemy import SQLAlchemy
from model import *

db.drop_all()
db.create_all()
bob = User('Bob', 'Hello this is Bob')
db.session.add(bob)
db.session.commit()

#action below

image1 = PhotoInfo('Splash', 'Los Altos', '2013', 'IMG_9696.jpg', 'action')
db.session.add(image1)
db.session.commit()

image2 = PhotoInfo('Chasing Yellow', 'Los Altos', '2013', 'IMG_9715.jpg', 'action')
db.session.add(image2)
db.session.commit()


#nature below

image3= PhotoInfo('Water crown', 'Oahu', '2014', 'IMG_1061.jpg', 'nature')
db.session.add(image3)
db.session.commit()

image4= PhotoInfo('(unknown)', 'Oahu', '2014', 'IMG_1116.jpg', 'nature')
db.session.add(image4)
db.session.commit()

image5= PhotoInfo('Sunset Chopper', 'Coronado', '2012', 'IMG_2481.jpg', 'nature')
db.session.add(image5)
db.session.commit()

image6= PhotoInfo('Glow of Gloriaetta Night ', 'Coronado', '2012', 'IMG_2532.JPG', 'nature')
db.session.add(image6)
db.session.commit()

image7= PhotoInfo('Collision', 'Oahu', '2014', 'nature large.jpg', 'nature')
db.session.add(image7)
db.session.commit()



#lifestyle below

image8= PhotoInfo('The Defenders', 'Los Altos', '2013', 'IMG_0389.jpg', 'lifestyle')
db.session.add(image8)
db.session.commit()

image9= PhotoInfo('Up', 'Los Altos', '2013', 'IMG_9599.jpg', 'lifestyle')
db.session.add(image9)
db.session.commit()

#sports below

image10= PhotoInfo('Surf', 'Oahu', '2014', 'G0020768.JPG', 'sports')
db.session.add(image10)
db.session.commit()














