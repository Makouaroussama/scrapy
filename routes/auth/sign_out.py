from app import app

@app.route("/api/auth/signout")
def signout():
    return ""