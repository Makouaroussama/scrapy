from app import auth
from flask import make_response

@auth.route("/signout", methods=["POST", "GET"])
def signout():
    # set auth token session or cookie to null and return an empty response
    res = make_response()
    res.set_cookie("user-token", None, max_age=0)
    res.status_code = 200

    return res