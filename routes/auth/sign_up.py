from app import app
from flask import request

@app.route("api/auth/signup")
def signup(): 
    email = request.form["email"]
    password = request.form["password"]
    
    # validate form data < email and password > and return error if they do not match criteria

    # check if a user with provided email already existed and return error if true

    # create new user and save it into db

    # generate a json web token
    
    # store it in session or a cookie
    
    # send back response with status code of 201 and user object as payload
    
    return ""