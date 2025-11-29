import time
from flask import Flask
from backend.server.extensions import db, cors
from backend.server.config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
cors.init_app(app)

from backend.models import data_models

with app.app_context():
    db.create_all()


@app.route("/time")
def get_current_time():
    return {"time": time.time()}
