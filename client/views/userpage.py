from flask import Blueprint, render_template

userpage = Blueprint('userpage', __name__, template_folder='templates',
                 static_folder='static')

userpage_url = 'userpage.html'

@userpage.route('/'+ userpage_url,  methods=['GET', 'POST'])
def display_userpage():
    return render_template(userpage_url)
