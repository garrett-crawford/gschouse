from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# uses the config.py file defined
app.config.from_object('config')

# our database object
# needs to be initialized when we initialize the app
db = SQLAlchemy(app)

from app import views, models