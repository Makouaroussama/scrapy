from werkzeug.wrappers import Request
from jwt import PyJWT
import os

class CurrentUser:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ=environ)
        userToken = req.cookies.get("user-token")
        try:
            payload = PyJWT.decode(jwt=userToken,key=os.getenv("JWT_KEY"), verify=True)
            environ["currentuser"] = payload
        except:
            environ["currentuser"] = None

        return self.app(environ, start_response)


        