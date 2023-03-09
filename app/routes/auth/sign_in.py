from app import auth
from flask import request, make_response, jsonify
from werkzeug.exceptions import BadRequest
import validators
from app.repositories.user_repo import UserRepository
from jwt import PyJWT
import os

@auth.route('/signin', methods=['POST'])
async def signIn():    
    email = request.form['email'].strip()
    password = request.form['password']

    if request.environ["currentuser"] != None:
        raise BadRequest("Already Sign In!")

    # validate form data < email and password > and return error if they do not match criteria
    if not validators.email(email):
        raise BadRequest("Email must be valid")
    
    if not validators.between(password, min=5, max=20):
        raise BadRequest("Password should be between 5 and 20 characters long")
    
    # search in db for a user with email and return error if no result was found
    user = await UserRepository.getUserByEmail(email)

    if user == None:
        raise BadRequest("Invalid Credentials")
    
    # compare user's password and password provided and return error if they do not match
    if not user.isSamePassword(password=password):
        raise BadRequest("Invalid Credentials")
    
    # create a response
    res = make_response(jsonify(user.dto))

    # generate a json web token
    userToken = PyJWT.encode(payload=user.payload, key=os.getenv("JWT_KEY"))

    # store it in session or a cookie
    res.set_cookie("user-token", userToken)

    # send back response with status code of 200 and user object as payload
    res.status_code = 200
    return res