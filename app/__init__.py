
from flask import Flask
from .config import DevConfig

#initializing flask

app = Flask(__name__, instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initializing flask extensions
bootstrap = Bootstrap(app) 


from app import views 