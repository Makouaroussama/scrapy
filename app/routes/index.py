from flask import make_response
from app import app as router

@router.route('/', methods=["GET", "POST"])
@router.route('/index', methods=["GET", "POST"])
def index():
    res = make_response({
        "message": "working as expected"
    })
    res.content_type = "application/json"
    res.status_code = 200
    return res;