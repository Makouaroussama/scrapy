from app import app

@app.route("/api/auth/signout")
def signout():
    # set auth token session or cookie to null and return an empty response
    return ""