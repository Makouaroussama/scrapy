from app import app
from flask import request, make_response
import jwt
import os

@app.route('/api/auth/currentuser')
def currentuser():
    authToken = request.cookies.get("auth_token")
    res = make_response("Response")

    if(authToken == None):
        res.data = {
            "currentuser": None
        }
        return res;
    
    try:
        payload = jwt.decode(authToken, os.getenv("JWT_KEY"))
        res.data = {
            "currentuser": payload
        }
    except:
        res.data = {
            "currentuser": None
        }

    return res

