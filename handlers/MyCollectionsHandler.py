from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from gaesessions import get_current_session
from helpers import TemplatedRequest, update_user_session, url_last_part
from helpers.decorators import login_required
from models.MovieCollection import MovieCollection
from models.Movie import Movie
from google.appengine.ext import db

class MyCollectionsHandler(webapp.RequestHandler, TemplatedRequest):
    @login_required
    def get(self, user):
        templ_vars = { 'user':user }
        url_ending = url_last_part(self.request.url)
        if (url_ending.isdigit()):
            collection = MovieCollection.get_by_id(int(url_ending))
            if collection:
                movies = Movie.get(collection.movies)
                assert not None in movies
                i = 0
                collection.movies = list()
                for key in movies:
                    collection.movies[i] = movies[i]
                    i = i + 1
            templ_vars['collection'] = collection
            return self.render_template('collection.html', templ_vars)
        
        return self.render_template('my_collections.html', templ_vars)

class NewCollectionHandler(webapp.RequestHandler, TemplatedRequest):
  @login_required
  def get(self, user):
    templ_vars = { 'user':user }
    return self.render_template('add_new_collection.html', templ_vars)
    
    
  def post(self):
    session = get_current_session()
    user = session.get('user')
    arg_title = self.request.get('title')
    arg_descr = self.request.get('description')
    if (arg_title is None) or (not arg_title):
      return self.response.out.write('need to enter title');
    
    if not arg_descr:
      return self.response.out.write('need to enter descr, can be empty');
      
    new_collection = MovieCollection(title=arg_title, description=arg_descr).put()
    user.movie_collections.append(new_collection)
    user.put()
    update_user_session(user)
    return self.redirect('/')
