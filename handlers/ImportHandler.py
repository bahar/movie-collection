from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from imdb import IMDb

class ImportHandler(webapp.RequestHandler):
    def get(self):
        arg_source = self.request.get('source')
        arg_title = self.request.get('title')
        if (arg_source is '') or (arg_title is ''):
            return self.response.out.write('no source or title')
        
        ia = IMDb()
        movie = ia.get_movie('0840361')
        if not movie:
            print 'no such movie'
        
        directors = movie['director']
        for person in directors:
            print person
        
        return self.response.out.write(movie['director'][0]['name'] + ' asd')
