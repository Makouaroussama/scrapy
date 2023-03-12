from flask import jsonify, make_response, Response
from werkzeug.exceptions import BadRequest, HTTPException
from app.errors.custom_bad_request import InvalidFormData
from app.configs import Config


def handleExceptions(e: Exception):    
    print("type of exc :", e)

    if isinstance(e, InvalidFormData):
        res = make_response(
            e.serialize()
        )
        res.set_cookie(Config.USER_TOKEN_KEY, "", max_age=0)
        return res

    if(isinstance(e, BadRequest)):   
        res = make_response({
            "description": BadRequest().description,
            "message": e.description,
            "error": e.code,
        })
        res.set_cookie(Config.USER_TOKEN_KEY, "", max_age=0)
        return res
    
    if(isinstance(e, HTTPException)):
        make_response({
            "description": HTTPException().description,
            "message": e.description,
            "code": e.code,
        })
        return res, e.code
    

    return make_response({"error occurred": type(e).__str__(e)})

    

