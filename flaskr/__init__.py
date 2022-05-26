# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from flaskr.myMap import MapViewUrl

# from myMap import Map


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/index')
def index():
    return render_template("base.html")


@app.route('/map')
def mapView():
    return render_template("map.html")
    # return render_template("map.html")


# context processors
@app.context_processor
def mapObj():
    return MapViewUrl("place")

# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()

