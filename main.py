import sys
if 'libs' not in sys.path:
    sys.path[0:0] = ['lib', 'distlib', 'distlib.zip', 'libs']
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from handlers.RootHandler import RootHandler
from handlers.ImportHandler import ImportHandler
from handlers.SignupHandler import SignupHandler
from handlers.LoginHandler import LoginHandler
from handlers.LogoutHandler import LogoutHandler
from handlers.MyCollectionsHandler import MyCollectionsHandler
from handlers.MyCollectionsHandler import NewCollectionHandler
from handlers.JSONIMDBHandler import JSONIMDBHandler


app = webapp.WSGIApplication(
  [
    ('/', RootHandler),
    ('/import', ImportHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/mycollections/add', NewCollectionHandler),
    ('/mycollections/.*', MyCollectionsHandler),
    ('/json/imdb', JSONIMDBHandler),
  ],
  debug=True)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', '')
TEMPLATE_ENV = Environment(loader = FileSystemLoader(TEMPLATE_PATH))

def render_template(filename, *args):
  template = TEMPLATE_ENV.get_template(filename)
  return template.render(*args)
  
def get_last_part_of_url(url):
  return url.

def main():
    run_wsgi_app(app)
    
def asd():
  return 'asd'

if __name__ == "__main__":
    main()
