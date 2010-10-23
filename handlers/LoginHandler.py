from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from gaeauth import hash_password
from google.appengine.ext import db
from models.User import User
from gaesessions import get_current_session
from helpers import render_template

class LoginHandler(webapp.RequestHandler):
    def get(self):
        session = get_current_session()
        if session.has_key('user'):
            return self.response.out.write('already logged in')
        else:
            self.response.out.write(render_template('login.html', {}))
    
    def post(self):
        arg_username = self.request.get('username')
        arg_password = self.request.get('password')
        hashed_pass = hash_password(arg_password)
        exist_user_query = db.GqlQuery("SELECT * FROM User WHERE username = '"+arg_username+"' AND hashed_pass = '"+hashed_pass+"'")
        exist_user = exist_user_query.fetch(1)
        if len(exist_user) is 0:
            return self.response.out.write("wrong info")
        else:
            session = get_current_session()
            if session.has_key('user'):
                return self.response.out.write("already logged")
            else:
                session['user'] = exist_user[0]
                return self.redirect("/")
  
