from flask import Blueprint, render_template

checkout = Blueprint('checkout', __name__, template_folder='templates',
                 static_folder='static')

checkout_url = 'checkout.html'

@checkout.route('/'+checkout_url,  methods=['GET', 'POST'])
def display_checkout():
    return render_template(checkout_url)
