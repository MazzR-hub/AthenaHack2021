from flask import Blueprint, render_template
from client.database import api

userpage = Blueprint('userpage', __name__, template_folder='templates',
                 static_folder='static')

userpage_url = 'account.html'

@userpage.route('/account',  methods=['GET', 'POST'])
def display_userpage():
    myBookings = api.get_user_details(000)
    if myBookings is None:
        myBookings = ["You have no bookings"]
    return render_template(userpage_url, myBookings=myBookings)

@userpage.route('/details', methods=['GET', 'POST'])
def display_details():
    return render_template('details.html')
