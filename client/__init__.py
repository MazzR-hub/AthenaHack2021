from flask import Flask
from flask_login import LoginManager
import sys 
sys.path.append("./views")

import homepage
#from client.views import homepage

import userpage
import checkout
import listings


app = Flask(__name__)
app.secret_key = 'shh'
login = LoginManager(app)

import login

app.register_blueprint(homepage)
app.register_blueprint(login)
app.register_blueprint(userpage)
app.register_blueprint(checkout)
app.register_blueprint(listings)
