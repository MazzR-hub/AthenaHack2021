from flask import Blueprint, render_template
from flask_login import current_user, login_user
#from client.modele import User
import sys
sys.path.append("../database")
import api

login = Blueprint('login', __name__, template_folder='templates',
                 static_folder='static')




@login.route('/login', methods=['GET', 'POST'])
def display_login():
    if current_user.is_authenticated:
        return redirect('/userpage')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/userpage')

    return render_template('login.html', title='Sign In', form=form)

@login.route('/signup', methods=['GET', 'POST'])
def display_signup():
    if current_user.is_authenticated:
        return redirect()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('signup.html', title='Register', form=form)

@login.route('/logout')
def logout():
    logout_user()
    return redirect('/home')
