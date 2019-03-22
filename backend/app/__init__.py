from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret*23@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://issue_tracker:today*123@127.0.0.1/issue_tracker'

db = SQLAlchemy(app)
ma = Marshmallow(app)
cors = CORS(app)
migrate = Migrate(app, db)

from app.user import model

from .user import user as user_blueprint
app.register_blueprint(user_blueprint, )


