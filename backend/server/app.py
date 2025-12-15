from flask import Flask
from backend.server.extensions import db, cors, ma, migrate
from backend.server.config import Config
from backend.routes.main import main


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
cors.init_app(app)
ma.init_app(app)
migrate.init_app(app, db, directory="backend/migrations")

import backend.models.data_models

app.register_blueprint(main)
