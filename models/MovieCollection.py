from google.appengine.ext import db

class MovieCollection(db.Model):
  ### ID IS ID ###
  title = db.StringProperty(required=True)
  description = db.StringProperty(required=True)
  movies = db.ListProperty(db.Key, required=True)

