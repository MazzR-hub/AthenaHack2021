from flask import Blueprint, render_template

listings = Blueprint('listings', __name__, template_folder='templates',
                 static_folder='static')

listings_url = 'listings.html'

@listings.route('/'+listings_url,  methods=['GET', 'POST'])
def display_listings():
    return render_template(listings_url)
