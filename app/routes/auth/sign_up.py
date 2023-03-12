from . import auth
from flask import make_response
from werkzeug.exceptions import BadRequest
from app.repositories.user_repo import UserRepository
from app.models.user import User
import jwt
from app.configs import Config
from app.types.credentials import Credentials
from app.processes.decorators.validate_form import validate_sign_form

@auth.route("/signup", methods=["POST"])
@validate_sign_form
def signup(cred: Credentials): 
    
    # check if a user with provided email already existed and return error if true
    existingUser = UserRepository.exists(email=cred.email)
    if existingUser:
        raise BadRequest("Email is already in use")
    
    # create new user and save it into db
    savedUser = UserRepository.save(user=User.fromCredentials(cred))
    
    # generate a json web token
    userToken = jwt.encode(payload=savedUser.payload(), key=Config.JWT_KEY, algorithm="HS256")
    # store it in session or a cookie
    res = make_response(savedUser.dto())
    res.set_cookie(Config.USER_TOKEN_KEY, userToken)
    # send back response with status code of 201 and user object as payload 
    return res, 201