import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def photography():
    return page('<strong>PHOTOGRAPHY!</strong>')

def page(html):
	return render_template('header.html') + html + render_template('footer.html')

