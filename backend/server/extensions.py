from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
ma = Marshmallow()
migrate = Migrate()
