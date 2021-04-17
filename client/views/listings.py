from flask import Blueprint, render_template
from client.database import api

listings = Blueprint('listings', __name__, template_folder='templates', static_folder='static')


@listings.route('/listings', methods=['GET', 'POST'])
def display_listings():
    listedItems = api.get_servicelist()
    if listedItems is None:
        listedItems = ['No listings available in your area! Why don\'t you add one?']
    return render_template('listings.html', listedItems=listedItems)
