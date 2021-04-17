from flask import Flask

from client.views.homepage import homepage
from client.views.login import login
from client.views.userpage import userpage
from client.views.checkout import checkout
from client.views.listings import listings


app = Flask(__name__)


app.register_blueprint(homepage)
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(userpage, url_prefix='/userpage')
app.register_blueprint(checkout, url_prefix='/checkout')
app.register_blueprint(listings, url_prefix='/listings')
