from flask_login import UserMixin
from client import login
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin): #db.Model):
    def __init__(self, uid, first_name, surname, email, password, membership, location_id):
        self.__uid = uid
        self.__first_name = first_name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__membership = membership
        self.location_id = location_id

        def get_uid(self):
            return self.__uid

        def get_first_name(self):
            return self.__first_name

        def get_surname(self):
            return self.__surname

        def get_email(self):
            return self.__email

        def get_password(self):
            return self.__password

        def get_membership(self):
            return self.__membership

        def get_location_id(self):
            return self.__location_id

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
