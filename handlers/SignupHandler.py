import config
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from gaeauth import hash_password
from google.appengine.ext import db
import main
from models.User import User

class SignupHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(main.render_template('signup.html', {}))
    
    def post(self):
        arg_username = self.request.get('username')
        arg_password = self.request.get('password')
        hashed_pass = hash_password(arg_password)
        exist_user_query = db.GqlQuery("SELECT * FROM User WHERE username = :1", arg_username)
        exist_user = exist_user_query.get()
        if exist_user is None:
            user = User(username=arg_username, hashed_pass=hashed_pass)
            user.put()
            return self.response.out.write("done")
        else:
            return self.response.out.write("exists")
        
