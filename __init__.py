from flask import Flask
from flask_login import LoginManager

exm = Flask(__name__)
exm.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager(exm)


from app import routes
