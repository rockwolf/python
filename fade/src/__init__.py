from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

from .views.home import home
from .views.control_panel import control_panel
from .views.finance import finance
from .views.test import test 

# Main config
app.config.from_object('config')
# Instance config, not checked in.
# Values here override the main config.
app.config.from_pyfile('config.py')
# Load config from env_var.
# Values here override the main config.
# See start.sh.
app.config.from_envvar('APP_CONFIG_FILE')
app.register_blueprint(home)
app.register_blueprint(control_panel)
app.register_blueprint(finance)
app.register_blueprint(test)


from src import views, models
