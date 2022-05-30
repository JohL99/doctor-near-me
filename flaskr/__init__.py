# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import socket
import re
import json
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
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = QueryForm()
    message = ""
    if form.validate_on_submit():
        query = form.query.data
        if query == "":
            # empty form field
            form.query.data = ""
            message = "No results found"
        else:
            form.query.data = ""
            queryObj = SearchQuery(query)
            queryString = queryObj.PrintQuery()
            return render_template("map.html", url=GetUrl(2, queryString), form=form, message=message)

    return render_template("map.html", url=GetUrl(1, GetLocation()), form=form, message=message)


@app.route('/test')
def test():
    return GetLocation()


# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()

