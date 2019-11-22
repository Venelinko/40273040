from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

main = Flask(__name__)
main.config.from_object(Config)
db = SQLAlchemy(main)
migrate = Migrate(main, db)

from app import routes, models