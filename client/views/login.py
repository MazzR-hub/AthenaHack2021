from flask import Blueprint, render_template

login = Blueprint('login', __name__, template_folder='templates',
                 static_folder='static')

login_url = 'login.html'
signup_url = 'signup.html'

@login.route('/'+login_url, methods=['GET', 'POST'])
def display_login():
    return render_template(login_url)

@login.route('/'+signup_url, methods=['GET', 'POST'])
def display_signup():
    return render_template(signup_url)
