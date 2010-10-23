from gaeauth import get_current_user

def login_required(handler_method):
    def check_login(self, *args):
        user = get_current_user()
        if not user:
            return self.redirect('/login')
        else:
            handler_method(self, *args)
    return check_login
