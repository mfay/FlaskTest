import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24) # os.environ['SECRET'] if os.environ.has_key('SECRET') else 'replace me!!!'

from flaskr.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.commit()
    db_session.remove()

import flaskr.views