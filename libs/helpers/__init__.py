from config import config
from gaesessions import get_current_session

class TemplatedRequest:
    def render_template(self, path, *args):
        return self.response.out.write(render_template(path, *args))

def render_template(filename, *args):
  template = config.TEMPLATE_ENV.get_template(filename)
  return template.render(*args)
  
def get_current_user():
    session = get_current_session()
    if session.has_key('user'):
        return session['user']

def update_user(new_user):
  get_current_session()['user'] = new_user
