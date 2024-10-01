from flask import Flask
import datetime
app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'
# app.permanent_session_lifetime = datetime.timedelta(minutes=1)


if __name__ == "__main__":
    app.run( debug=True) 