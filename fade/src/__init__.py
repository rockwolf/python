from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

# Main config
app.config.from_object('config')
# Instance config, not checked in.
# Values here override the main config.
app.config.from_pyfile('config.py')
# Load config from env_var.
# Values here override the main config.
# See start.sh.
app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)

from src import views, models
