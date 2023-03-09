from app import auth
from flask import request, make_response
from jwt import PyJWT
import os

@auth.route('/currentuser')
def currentuser():
    authToken = request.cookies.get("auth_token")
    res = make_response()
    res.data = {
        "currentuser": None
    }

    if(authToken == None):
        return res;
    
    try:
        payload = PyJWT.decode(authToken, os.getenv("JWT_KEY"))
        res.data = {
            "currentuser": payload
        }
    except:
        pass;

    return res

