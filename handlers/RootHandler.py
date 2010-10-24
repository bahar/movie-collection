from google.appengine.ext import webapp
import os
from helpers import render_template, get_current_user, grab_collections
from gaesessions import get_current_session
from models.User import User
from models.MovieCollection import MovieCollection
from models.Movie import Movie

class RootHandler(webapp.RequestHandler):
    def get(self):
      arg_method = self.request.get('method')
      user = get_current_user()
      if user:
          grab_collections(user)
      
      templ_vars = { 'user':user }
      if not arg_method:
        return self.response.out.write(render_template('root.html', templ_vars))
      
      if arg_method == 'delete':
        arg_what = self.request.get('what')
        if not arg_what:
          return self.request.out.write('no what specified.')
        
        if arg_what == 'users':
          all_users = User.all()
          for user in all_users:
            user.delete()
          return self.redirect('/')
          
        if arg_what == 'collections':
          all_colls = MovieCollection.all()
          for col in all_colls:
            col.delete()
          return self.redirect('/')
        
        if arg_what == 'movies':
          movies = Movie.all()
          for movie in movies:
            movie.delete()
          return self.redirect('/')
        
        if arg_what == 'user_session':
            get_current_session().terminate()
            return self.redirect('/')
        return self.response.out.write(' no valid what')
      
      return self.response.out.write(' no valid method')
            

