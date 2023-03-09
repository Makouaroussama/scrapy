from . import routes
from flask import request, make_response
import jwt
import os

@routes.route('/api/auth/currentuser')
def currentuser():
    authToken = request.cookies.get("auth_token")
    res = make_response()
    res.data = {
        "currentuser": None
    }

    if(authToken == None):
        return res;
    
    try:
        payload = jwt.decode(authToken, os.getenv("JWT_KEY"))
        res.data = {
            "currentuser": payload
        }
    except:
        pass;

    return res

