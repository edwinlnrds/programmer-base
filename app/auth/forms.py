from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = TextField('Username', id='username', validators=[DataRequired()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    remember = BooleanField('Remember me')

class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username', validators=[DataRequired()])
    email = TextField('Email', id='email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[DataRequired(), EqualTo('password', message='Confirmation password must match password')])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    title = TextField('Title', id='title', validators=[DataRequired()])
    content = TextField('Content', id='content', validators=[DataRequired()])

    