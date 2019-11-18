from flask import Flask
from .config import DevelopmentConfig
from flask_bootstrap import Bootstrap

#initialization of the application
app = Flask(__name__,instance_relative_config = True)

# configurations settings
app.config.from_object(DevelopmentConfig)
app.config.from_pyfile('config.py')

#initializing flask extensions
bootstrap = Bootstrap(app)

from app import views