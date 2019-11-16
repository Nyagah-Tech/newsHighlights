from flask import Flask
from .config import DevelopmentConfig
#initialization of the application
app = Flask(__name__)

# configurations settings
app.config.from_object(DevelopmentConfig)
from app import views