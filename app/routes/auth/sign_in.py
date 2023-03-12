from . import auth
from flask import request, make_response
from werkzeug.exceptions import BadRequest
from app.repositories.user_repo import UserRepository
from app.configs import Config
from app.processes.decorators.validate_form import validate_sign_form
from app.types.credentials import Credentials
import jwt

@auth.route('/signin', methods=['POST'])
@validate_sign_form
def signIn(credentials: Credentials):    
    
    # check if the current user is already signed in if so return an error or a success response
    currentuser = request.environ["currentuser"]
    if currentuser != None and credentials.email == currentuser["email"]:
        raise BadRequest("Already Signed In!")
    
    # search in db for a user with email and return error if no result was found
    user = UserRepository.getUserByEmail(credentials.email)

    if user == None:
        raise BadRequest("Invalid Credentials")
    
    # compare user's password and password provided and return error if they do not match
    if not user.isPasswordMatched(password=credentials.password):
        raise BadRequest("Invalid Credentials")
    
    # create a response
    res = make_response(user.dto())

    # generate a json web token
    userToken = jwt.encode(payload=user.payload(), key=Config.JWT_KEY, algorithm="HS256")
    
    # store it in session or a cookie
    res.set_cookie(Config.USER_TOKEN_KEY, userToken)

    # send back response with status code of 200 and user object as payload
    return res, 200