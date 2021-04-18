from flask import Blueprint, render_template
from flask_login import current_user, login_user
from client.models import User, RegistrationForm, LoginForm
from client.database import api

login = Blueprint('login', __name__, template_folder='templates',
                 static_folder='static')




@login.route('/login', methods=['GET', 'POST'])
def display_login():
    if current_user.is_authenticated:
        return redirect('/userpage')
    form = LoginForm()
    if form.validate_on_submit():

        #doesn't work
        return redirect('/home')

    return render_template('login.html', title='Sign In', form=form)

@login.route('/signup', methods=['GET', 'POST'])
def display_signup():
    if current_user.is_authenticated:
        return redirect()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, first_name=form.first_name.data, surname=form.surname.data, password=from.password.data, membership=false, locId=1)
        new_id = api.add_user(user)
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('signup.html', title='Register', form=form)

@login.route('/logout')
def logout():
    logout_user()
    return redirect('/home')
