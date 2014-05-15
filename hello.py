
import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
from model import *




@app.route('/all_users')
def double_hello():
    users = User.query.all()

    output = ""
    for user in users:
        output += "<p>"+str(user.id) +" "+ user.username + " " + user.message + "</p>"
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

	photoList = []
	for root, dirs, files in os.walk("./static/images/Photos/"+ category):
		for file in files:
			if file.endswith(".jpg") or file.endswith (".JPG"):
				 photoList.append(os.path.join(root[1:], file))

	return page(render_template('photos.html', photos = photoList))


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