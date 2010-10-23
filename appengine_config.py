import config
from gaesessions import SessionMiddleware
import os
COOKIE_KEY = "'~~ \xfb\xaa\xf3\xe0\xffl\xa7\x00&\xc4\xee\xf3\xaf\xf6S\xe5$v\x96\xf3\x89\xbd\x93\xfe\xceE<\xe9\xc0\xf8\x06\x0fn\x91\xb3\xbcyO\xd9\x07\xac\xf3^\x1a\xe60\xa5\xe2\xb8'\"\xed\x9b?N\x7fbq|\xce&\x94'"

def webapp_add_wsgi_middleware(app):
  from google.appengine.ext.appstats import recording
  app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
  app = recording.appstats_wsgi_middleware(app)
  return app
