from flask import jsonify, make_response
from werkzeug.exceptions import BadRequest

def handleExceptions(e: Exception):
    res = make_response({
        "message": "an error has occurred",
        "error": e.description
    })

    if(isinstance(e, BadRequest)):
        res.status_code = 400

    return res;


