from app import app
from flask import request

@app.route('/api/auth/signin', methods=['POST'])
def signIn():    
    email = request.form['email']
    password = request.form['password']

    # validate form data < email and password > and return error if they do not match criteria

    # search in db for a user with email and return error if not result was found
    
    # compare user's password and password provided and return error if they do not match
    
    # generate a json web token
    
    # store it in session or a cookie
    
    # send back response with status code of 200 and user object as payload

    return ""