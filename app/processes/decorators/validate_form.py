from functools import wraps
from flask import request
from app.errors.custom_bad_request import FormInputError, InvalidFormData
from app.types.credentials import Credentials
import validators

def validate_sign_form(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # validate form data < email and password > and return error if they do not match criteria
        inputErrors: list[FormInputError] = []
        if("email" not in request.form):
            inputErrors.append(FormInputError("email", "email address field must have a value.", "please enter a valid address email."))
        
        if("password" not in request.form):
            inputErrors.append(FormInputError("password", "password field must have a value.", "please enter a fairly strong password."))
        
        if(inputErrors.__len__() > 0):
            raise InvalidFormData(inputErrors, "some fields left empty!")
        
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        if not validators.email(email):
            inputErrors.append(FormInputError("email", "email address has to be in a right format", "an example of a valid email is: username@example.com"))
        
        if not validators.between(password.__len__(), min=5, max=20):
            inputErrors.append(FormInputError("password", "this password is vulnerable and easy to break", "an example of a strong password is: Bruh!34_sT [min_length: 5, max_length: 20]"))
        
        if(inputErrors.__len__() > 0):
            raise InvalidFormData(inputErrors, "some fields need a second look")
        
        credentials = Credentials(email, password)
        return f(credentials, *args, **kwargs)
    return decorator
