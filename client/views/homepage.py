from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, template_folder='templates',
                      static_folder='static')

homepage_url = 'index.html'

@homepage.route('/')
@homepage.route('/'+homepage_url)
def display():
    return render_template(homepage_url)
