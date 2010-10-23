from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from gaeauth import hash_password
from google.appengine.ext import db
from models.User import User
from gaesessions import get_current_session

class LogoutHandler(webapp.RequestHandler):
    def get(self):
        session = get_current_session()
        if session.has_key('user'):
            del session['user']
            return self.response.out.write('logged out')
        else:
            return self.response.out.write('was not logged in')
