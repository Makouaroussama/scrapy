from werkzeug.wrappers import Request
import jwt
import os

class CurrentUser:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ=environ)
        userToken = req.cookies.get("user-token")
        try:
            payload = jwt.decode(jwt=userToken,key=os.getenv("JWT_KEY"), algorithms=["HS256"])
            environ["currentuser"] = payload
        except:
            environ["currentuser"] = None

        return self.app(environ, start_response)


        