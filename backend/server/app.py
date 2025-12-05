from flask import Flask
from backend.server.extensions import db, cors, ma
from backend.server.config import Config
from backend.routes.main import main


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
cors.init_app(app)
ma.init_app(app)

from backend.models import data_models

with app.app_context():
    db.create_all()

app.register_blueprint(main)
