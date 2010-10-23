from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import sys
import imdb
import simplejson as json
from gaeimdb import search_movies

class JSONIMDBHandler(webapp.RequestHandler):
    def get(self):
      method = self.request.get('method')
      if not method:
        return self.response.out.write('no method given')
      
      if method == 'get_matching_titles':
        title = self.request.get('title')
        if not title:
          return self.response.out.write('this method needs title parameter.')
          
        
          
        
        response = search_movies(title)
        if len(response) == 0:
          return self.response.out.write('')
        return self.response.out.write(json.dumps(response))
        
          
          
          
          
          
        i = imdb.IMDb(accessSystem='http')
        results = i.search_movie(title)
        if not results:
          return self.response.out.write('')
        response = list()
        for movie in results:
          response.append({'id':movie.movieID, 'long_title':movie['long imdb title']})
        return self.response.out.write(json.dumps(response))
      
      if method == 'get_movies':
        arg_movie_ids = self.request.get('movieIDs');
        if not arg_movie_ids:
          return self.response.out.write('this method needs movieids parameter.');
        
        i = imdb.IMDb(accessSystem='http')
        movie_ids = arg_movie_ids.split(',');
        response = list();
        for movie_id in movie_ids:
          movie = i.get_movie(movie_id);
          response.append({'title':movie['title'],'genres':movie['genres']})
        return self.response.out.write(response)
      
      return self.response.out.write('method not supported')

