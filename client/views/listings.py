from flask import Blueprint, render_template

listings = Blueprint('listings', __name__, template_folder='templates',
                 static_folder='static')


@listings.route('/listings')
def display_listings():
    return render_template('listings.html')
