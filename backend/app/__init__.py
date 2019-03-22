from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = "Flask@!123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://issue_tracker:issue*127.0.0.1/issue_tracker'

db = SQLAlchemy(app)
ma = Marshmallow()
cors = CORS(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)


from app.departments import departments

app.register_blueprint(departments)
