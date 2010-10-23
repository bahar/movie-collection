from helpers import get_current_user, render_template
from google.appengine.ext import webapp

def login_required(f):
    def wrapper(caller):
        user = get_current_user()
        if user:
            return f(*args)
        else:
            return f
    return wrapper

def guest_required(f):
    def wrapper(handler):
        user = get_current_user()
        if user:
            context = {
                'error':'You are already logged in!'
            }
            return handler.response.out.write(render_template('error_general.html', context))
        else:
            return f()
    return wrapper
