from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

pathname = os.path.abspath(os.path.dirname(__file__))
obj = Flask(__name__)
obj.config.from_mapping(
    SECRET_KEY='im-batman',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(pathname, 'app.db')
)
db = SQLAlchemy(obj)

#these 3 lines auto gen database
with obj.app_context():
    from app.models import User
    db.create_all()

from app import routes
