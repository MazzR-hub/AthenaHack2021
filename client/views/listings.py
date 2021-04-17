from flask import Blueprint, render_template

listings = Blueprint('listings', __name__, template_folder='templates', static_folder='static')


@listings.route('/listings', methods=['GET', 'POST'])
def display_listings():
    listedItems = ['hi', 'you', 'suck']
    return render_template('listings.html', listedItems=listedItems)
