from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager.init_app(app)

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app import views, models