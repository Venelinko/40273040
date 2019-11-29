from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

main = Flask(__name__)
main.config.from_object(Config)
db = SQLAlchemy(main)
migrate = Migrate(main, db)
login = LoginManager(main)
login.login_view = 'login'

from app import routes, models