from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash
from flask_login import LoginManager
import os

# Create the application object
app = Flask(__name__)

# Create a Bycryp instance
bcrypt = Bcrypt(app)

# Create a LoginManager instance and configure for login
login_manager = LoginManager()
login_manager.init_app(app)

#  Development environment
app.config.from_object(os.environ['APP_SETTINGS'])

# Create the sqlalchemy object
db = SQLAlchemy(app)

from app.auth.views import auth_blueprint
from app.main.views import main_blueprint
from app.store.views import store_blueprint

# register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(store_blueprint)


from models import User

login_manager.login_view = "auth.login"


# Load user from database and store user_id as the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
