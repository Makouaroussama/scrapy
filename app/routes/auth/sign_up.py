from app import auth
from flask import request, make_response
import validators
from werkzeug.exceptions import BadRequest
from app.repositories.user_repo import UserRepository
from app.models.user import User
from jwt import PyJWT
import os

@auth.route("/signup", methods=["POST"])
async def signup(): 
    email = request.form["email"]
    password = request.form["password"]
    
    # validate form data < email and password > and return error if they do not match criteria
    if not validators.email(email):
        raise BadRequest("Email must be valid")
    
    if not validators.between(password.__len__(), min=5, max=20):
        raise BadRequest("Password should be between 5 and 20 characters long")
    
    # check if a user with provided email already existed and return error if true
    existingUser = UserRepository.exists(email=email)
    if existingUser:
        raise BadRequest("Email is already in use")
    
    # create new user and save it into db
    savedUser = await UserRepository.save(user=User(email=email, password=password))
    
    # generate a json web token
    userToken = PyJWT.encode(payload=savedUser.payload, key=os.getenv("JWT_KEY"))
    # store it in session or a cookie
    res = make_response(savedUser.dto)
    res.set_cookie('user-token', userToken)
    # send back response with status code of 201 and user object as payload
    res.status_code = 201
 
    return res 