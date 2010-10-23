from google.appengine.ext import db

class Movie(db.Model):
    name = db.StringProperty(required=True)
    director = db.StringProperty()
    more_attrs = db.StringListProperty()

