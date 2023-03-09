from flask import Flask, Blueprint

app = Flask(__name__)
auth = Blueprint('auth', __name__, url_prefix="/api/auth")

from app.routes.auth.current_user import currentuser
from app.routes.auth.sign_in import signIn
from app.routes.auth.sign_up import signup
from app.routes.auth.sign_out import signout
from .routes.index import index 

app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)