from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', id='username',
                           validators=[DataRequired()])
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember me', id='remember')
    submit = SubmitField('Login')


class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username',
                           validators=[DataRequired()])
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()])
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[
                                     DataRequired(), EqualTo('password', message='Confirmation password must match password')])
    submit = SubmitField('Register')


class PostForm(FlaskForm):
    title = StringField('Title', id='title', validators=[DataRequired()])
    content = TextAreaField('Content', id='content', validators=[DataRequired()])
    tag = StringField('Tag', id='tag')
    submit = SubmitField('Create Post')

class EditProfile(FlaskForm):
    pass