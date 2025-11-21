from dotenv import load_dotenv
import os
import time
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


class Config(object):
    """Set enviroment variables"""

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)
CORS(app)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


@app.route("/time")
def get_current_time():
    return {"time": time.time()}
