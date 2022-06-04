# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import socket, re, json
from urllib.request import urlopen

from flaskr.myMap import GetUrl, QueryForm, SearchQuery, GetLocation



# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# Encryption key for flask-wtf
app.config['SECRET_KEY'] = 'thisissecret'

# Flask-Bootstrap requires this line
Bootstrap(app)

@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template("base.html")


@app.route('/map', methods=['GET', 'POST'])
def mapView():
    form = QueryForm()
    return render_template("map.html", url=GetUrl(1, GetLocation()), form=form)


@app.route('/QueryHandler/', methods=['post'])
def QueryHandler():
    form = QueryForm()
    if form.validate_on_submit():
        url = GetUrl(3, form.query.data)
        return url
    return jsonify(data=form.errors)


@app.route('/test')
def test():
    return GetLocation()


# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()

