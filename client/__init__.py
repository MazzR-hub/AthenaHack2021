from flask import Flask
from flask_login import LoginManager

from client.views.homepage import homepage

from client.views.userpage import userpage
from client.views.checkout import checkout
from client.views.listings import listings


app = Flask(__name__)
app.secret_key = 'shh'
login = LoginManager(app)

app.static_folder = 'static'

from client.views.login import login

app.register_blueprint(homepage)
app.register_blueprint(login)
app.register_blueprint(userpage)
app.register_blueprint(checkout)
app.register_blueprint(listings)
