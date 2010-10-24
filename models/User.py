from google.appengine.ext import db
from models.MovieCollection import MovieCollection
class User(db.Model):
    ### ID IS USER ID ###
    username = db.StringProperty(required=True)
    hashed_pass = db.StringProperty(required=True)
    movie_collections = db.ListProperty(db.Key, required=True)

