from google.appengine.ext import db

class User(db.Model):
  username = db.StringProperty(required=True)
  hashed_pass = db.StringProperty(required=True)
  movie_collections = db.ListProperty(db.Key, required=True)
