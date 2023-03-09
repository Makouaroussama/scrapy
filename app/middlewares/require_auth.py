from werkzeug.wrappers import Request, Response

class RequireAuth:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ=environ)

