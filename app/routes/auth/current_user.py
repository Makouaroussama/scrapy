from app import auth
from flask import request, make_response

@auth.route('/currentuser')
def currentuser():
    res = make_response({"currentuser": request.environ["currentuser"]})
    return res

