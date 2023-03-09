from flask import Flask, Blueprint
from .middlewares.error_handler import handleExceptions 
from .middlewares.current_user import CurrentUser 
import os
app = Flask(__name__)

# setting up routes and blueprints
auth = Blueprint('auth', __name__, url_prefix="/api/auth")

from app.routes.auth.current_user import currentuser
from app.routes.auth.sign_in import signIn
from app.routes.auth.sign_up import signup
from app.routes.auth.sign_out import signout
from .routes.index import index 

app.register_blueprint(auth)

# setting error handling
app.register_error_handler(400, handleExceptions)

# setting middlewares
app.wsgi_app = CurrentUser(app.wsgi_app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="3002", debug=True)