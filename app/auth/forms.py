from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = TextField('Username', id='username', validators=[DataRequired()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    remember = BooleanField('Remember me')

class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username', validators=[DataRequired()])
    email = TextField('Email', id='email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[DataRequired(), EqualTo('Password', message='Confirmation password must match password')])