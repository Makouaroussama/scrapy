from . import auth
from flask import request, make_response
from werkzeug.exceptions import BadRequest
import validators
from app.repositories.user_repo import UserRepository
import jwt
import os

@auth.route('/signin', methods=['POST'])
def signIn():    
    email = request.form['email'].strip().lower()
    password = request.form['password']

    # validate form data < email and password > and return error if they do not match criteria
    if not validators.email(email):
        raise BadRequest("Email must be valid")
    
    if not validators.between(password.__len__(), min=5, max=20):
        raise BadRequest("Password should be between 5 and 20 characters long")
    
    # check if the current user is already signed in if so return an error or a success response
    currentuser = request.environ["currentuser"]
    if currentuser != None and email == currentuser["email"]:
        raise BadRequest("Already Signed In!")
    
    # search in db for a user with email and return error if no result was found
    user = UserRepository.getUserByEmail(email, test=False)

    if user == None:
        raise BadRequest("Invalid Credentials")
    
    # compare user's password and password provided and return error if they do not match
    if not user.isPasswordMatched(password=password):
        raise BadRequest("Invalid Credentials")
    
    # create a response
    res = make_response(user.dto())

    # generate a json web token
    userToken = jwt.encode(payload=user.payload(), key=os.getenv("JWT_KEY"), algorithm="HS256")
    
    # store it in session or a cookie
    res.set_cookie("user-token", userToken)

    # send back response with status code of 200 and user object as payload
    return res, 200