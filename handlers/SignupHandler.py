import config
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from gaeauth import hash_password
from google.appengine.ext import db
from helpers import render_template, get_current_user, TemplatedRequest
from helpers.decorators import guest_required
from models.User import User


class SignupHandler(webapp.RequestHandler, TemplatedRequest):
    
    @guest_required
    def get(self):
        user = get_current_user()
        if user:
            return self.redirect()
        else:
            return self.response.out.write(render_template('signup.html', {}))
    
    def post(self):
        arg_username = self.request.get('username')
        arg_password = self.request.get('password')
        hashed_pass = hash_password(arg_password)
        existing_user = User.all().filter('username = ', arg_username).get()
        if existing_user is None:
            user = User(username=arg_username, hashed_pass=hashed_pass).put()
            return self.redirect("/")
        else:
            context = {
                'exists':True
            }
            return self.response.out.write(render_template('signup.html', context))
