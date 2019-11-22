from flask import Flask
from config import Config

main = Flask(__name__)
main.config.from_object(Config)

from app import routes