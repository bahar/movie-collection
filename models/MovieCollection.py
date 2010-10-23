from google.appengine.ext import db

class MovieCollection(db.Model):
  cid = db.IntegerProperty(required=True)
  title = db.StringProperty(required=True)
  description = db.StringProperty(required=True)
  collection = db.ListProperty(db.Key, required=True)

