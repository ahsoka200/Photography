import os
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return page('<strong>Home</strong>')

def page(html):
	return render_template('header.html') + html + render_template('footer.html')

@app.route('/photos')
def photos():
	photoList = []
	for root, dirs, files in os.walk("./static/images/photos"):
		for file in files:
			if file.endswith(".jpg") or file.endswith (".JPG"):
				 photoList.append(os.path.join(root, file))

	return page(render_template('photos.html', photos = photoList))
	#return page(output)

@app.route('/videos')
def videos():
	return page(render_template('coming-soon.html'))

@app.route('/digitalart')
def digitalArt():
	return page('<strong>DigitalArt</strong>')

@app.route('/about')
def about():
	return page(render_template('about.html'))

@app.route('/store')
def store():
	return page(render_template('coming-soon.html'))