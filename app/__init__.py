from flask import Flask
from .config import DevelopmentConfig
#initialization of the application
app = Flask(__name__,instance_relative_config = True)

# configurations settings
app.config.from_object(DevelopmentConfig)
app.config.from_object('config.py')

from app import views