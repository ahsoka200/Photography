import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
from flask import request
import PIL
from PIL import Image



app = Flask(__name__)
app.debug = True

#app.config.from_object('config')
if 'DATABASE_URL' in os.environ:
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hjjfqpndngobor:NvFLJbOkjm3tIIjC_lR1ovcRPd@ec2-54-225-101-119.compute-1.amazonaws.com:5432/d8foksvgpa5qav'
db = SQLAlchemy(app)
from model import *




# @app.route('/all_users')
# def double_hello():
#     users = User.query.all()

#     output = ""
#     for user in users:
#         output += "<p>"+str(user.id) +" "+ user.username + " " + user.message + "</p>"
#     return "this is what was found: " + output



@app.route('/all_photos')
def show_all_photos():
    photoinfos = PhotoInfo.query.filter(PhotoInfo.category=='action')

    output = ""
    for photo in photoinfos:
        output += "<p>"+str(photo.id) +" "+ photo.title + " " + photo.place + " " + photo.year + " " + photo.path + " " + photo.category + "</p>"
    return "this is what was found: " + output




@app.route('/')
def home():
    return page(render_template('home.html'))

def page(html):
	return render_template('header.html') + html + render_template('footer.html')

@app.route('/photos')
def photos():
	
	return page(render_template('photo-categories.html'))

@app.route('/photos/<category>')
def photo_category(category):

	photoList = PhotoInfo.query.filter(PhotoInfo.category == category)
	#for root, dirs, files in os.walk("./static/images/Photos/"+ category):
	#	for file in files:
	#		if file.endswith(".jpg") or file.endswith (".JPG"):
	#			 photoList.append(os.path.join(root[1:], file))

	photosJSON = []
	for p in photoList:
		photosJSON.append(p.serialize())

	return page(render_template('photos.html', photos = photoList, photosJSON = photosJSON))


@app.route('/videos')
def videos():
	return page(render_template('coming-soon.html'))

@app.route('/digitalart')
def digitalArt():
	return page(render_template('coming-soon.html'))

@app.route('/about')
def about():
	return page(render_template('about.html'))

@app.route('/store')
def store():
	return page(render_template('coming-soon.html'))

@app.route('/newphoto')
def newPhoto():
	return page(render_template('new-photo.html'))

@app.route('/uploadphoto', methods=['GET',  'POST'])
def uploadPhoto():
	if request.method == 'POST':
		title = request.form['title']
		place = request.form['place']
		year = request.form['year']
		category = request.form['category']
		f = request.files['photoFile']

		#add to database
		image = PhotoInfo(title, place, year, f.filename, category)
		db.session.add(image)
		db.session.commit()

		#add to databasecreation.py
		with open("databasecreation.py", "a") as pythonfile:
			pythonfile.write("image = PhotoInfo('"+title+"', '"+place+"', '"+year+"', '"+f.filename+"', '"+category+"')\n")
			pythonfile.write("db.session.add(image)\n")
			pythonfile.write("db.session.commit()\n\n")


		#saves the photo in the corect spot.
		#img = Image.open(StringIO(f))
		f.save('/Users/Chris/code/Photography/static/images/Photos/' + f.filename)
		img = Image.open('/Users/Chris/code/Photography/static/images/Photos/' + f.filename)
		width,height = img.size
		imgbig = img.resize((width*1000/height, 1000), Image.ANTIALIAS)
		imgbig.save('/Users/Chris/code/Photography/static/images/Photos/' + f.filename)

		imgzzz = img.resize((width*244/height, 244), Image.ANTIALIAS)
		imgzzz.save('/Users/Chris/code/Photography/static/images/Photos/zzz' + f.filename)



		return page(render_template('uploadphoto.html'))








