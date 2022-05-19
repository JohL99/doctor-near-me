# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

from src import objects as maps


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
    mapInst = maps.maps.GMAPS("JohL99.za@ganil.com", "")
    return render_template("map.html", mapInst=mapInst)


# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()
