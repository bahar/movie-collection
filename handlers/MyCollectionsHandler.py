from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from gaesessions import get_current_session
from helpers import TemplatedRequest, update_user
from helpers.decorators import login_required
from models.MovieCollection import MovieCollection
from google.appengine.ext import db

class MyCollectionsHandler(webapp.RequestHandler, TemplatedRequest):
    @login_required
    def get(self):
        session = get_current_session()
        user = session.get('user')
        collections = db.get(user.movie_collections)
        templ_vars = { 'user':user,'collections':collections }
        return self.render_template('my_collections.html', templ_vars)

class NewCollectionHandler(webapp.RequestHandler, TemplatedRequest):
  @login_required
  def get(self):
    session = get_current_session()
    user = session.get('user')
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
    
    query = db.GqlQuery("SELECT * FROM MovieCollection ORDER BY cid DESC")
    result = query.fetch(1)
    #return self.response.out.write(str(result))
    if (len(result) == 0):
      next_cid = 1
    else:
      next_cid = result[0].cid + 1
    new_collection = MovieCollection(cid=next_cid, title=arg_title, description=arg_descr)
    new_collection.put()
    user.movie_collections.append(new_collection.key())
    user.put()
    update_user(user)
    return self.redirect('/')
