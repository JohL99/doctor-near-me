# ---------------------------------------------------------------------------------------------------------------------------------
# Map View source
# TODO: mark major medical facilities on the map
# ---------------------------------------------------------------------------------------------------------------------------------

from flaskr.config import MapApi 
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import socket
import re
import json
from urllib.request import urlopen


# ---------------------------------------------------------------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------------------------------------------------------------

MODE_PLACE = "place"
MODE_SEARCH = "search"
ZOOM = 9
MedicalTerms = [
                "hospital", "doctor", "dentist",
                "psychologist", "psychiatrist", "surgeon",
                "gp", "general practitioner", "xray",
                "radiologist", "cardiologist", "gastro-enterologist",
                "plastic surgeon", "medical", "medical center", 
                "medical centre"
                ]

# ---------------------------------------------------------------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------------------------------------------------------------

# map view of a specific location
def MapViewUrl_1(mode, mapCenter, zoom):
    key = MapApi["key"]
    url_part = 'https://www.google.com/maps/embed/v1/{mode}?key={key}&center={mapCenter}&zoom={zoom}'
    url = url_part.format(mode=mode, key=key, mapCenter=mapCenter, zoom=zoom)
    urlDict = {
        "url": url
    }
    return urlDict


# map view of a specific location, and zoom level
def MapViewUrl_2(mode, location, zoom):
    key = MapApi["key"]
    url_part = 'https://www.google.com/maps/embed/v1/{mode}?key={key}&q={location}&zoom={zoom}'
    url = url_part.format(mode=mode, key=key, location=location, zoom=zoom)
    urlDict = {
        "url": url
    }
    return urlDict


    # search view
def MapViewUrl_3(mode, location, zoom):
    key = MapApi["key"]
    url_part = 'https://www.google.com/maps/embed/v1/{mode}?key={key}&q={location}&zoom={zoom}'
    url = url_part.format(mode=mode, key=key, location=location, zoom=zoom)
    urlDict = {
        "url": url
    }
    return urlDict


# Choose which map view to use
def GetUrl(view, query):
    url = ''
    CurrLocation = GetLocation()
    match view:
        case 1:
            url = MapViewUrl_1("view", CurrLocation, 500)
            return url
        case 2:
            url = MapViewUrl_2(MODE_PLACE, query, ZOOM)
            return url
        case 3:
            url = MapViewUrl_3(MODE_SEARCH, query, ZOOM)
            return url
        case _:
            return "Something went wrong"


# get users current location using geopy
def GetLocation():
    # Get the hostname by socket.gethostname() and IP address using socket.gethostbyname() method
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # Get the coords from ip address
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    location = data['loc']
    return location

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------------------------------------------------------------------------

# Class for query form
class QueryForm(FlaskForm):
    query = StringField('Search for a medical professional near you.', validators=[DataRequired()])


# Class for query
class SearchQuery:
    def __init__(self, query):
        self.query = query
        self.query_list = query.split(" ")
        self.query_list_len = len(self.query_list)
        self.query_list_index = 0
        self.query_list_index_max = self.query_list_len - 1
        self.query_list_index_min = 0
        self.query_list_index_range = self.query_list_index_max - self.query_list_index_min

    def next(self):
        if self.query_list_index < self.query_list_index_max:
            self.query_list_index += 1
        else:
            self.query_list_index = self.query_list_index_min
        return self.query_list[self.query_list_index]

    def prev(self):
        if self.query_list_index > self.query_list_index_min:
            self.query_list_index -= 1
        else:
            self.query_list_index = self.query_list_index_max
        return self.query_list[self.query_list_index]

    def PrintQuery(self):
        return self.query

# ------------------------------------------------------------------------------------------------------------------------------------------------
# test space 
# ------------------------------------------------------------------------------------------------------------------------------------------------

"""
    SearchQuery_1 = SearchQuery("Eiffel Tower")
    SearchQuery_2 = SearchQuery("Eiffel Tower Paris")
    print(SearchQuery_1.get_query())
    query1 = SearchQuery_2.next()
    print(query1)
    query2 = SearchQuery_2.next()
    print(query2)
"""
