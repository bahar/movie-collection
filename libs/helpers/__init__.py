from config import config
from gaesessions import get_current_session
from models.User import User
import string

class TemplatedRequest:
    def render_template(self, path, *args):
        return self.response.out.write(render_template(path, *args))

def render_template(filename, *args):
  template = config.TEMPLATE_ENV.get_template(filename)
  return template.render(*args)

def update_user_session(new_user=None):
    if new_user is None:
        old_user = get_current_user()
        if not old_user:
            return None
        new_user = User.get_by_id(old_user.key().id())
    get_current_session()['user'] = new_user

def get_current_user():
    session = get_current_session()
    if session.has_key('user'):
        return session['user']
    else:
        return None

def url_last_part(url):
    return url[string.rfind(url,'/')+1:len(url)+1]
    
def grab_collections(user):
    from models.MovieCollection import MovieCollection
    collections = MovieCollection.get(user.movie_collections)
    assert not None in collections
    i = 0
    for key in user.movie_collections:
        user.movie_collections[i].title = collections[i].title
        user.movie_collections[i].description = collections[i].description
        user.movie_collections[i].id = collections[i].key().id()
        i = i + 1
