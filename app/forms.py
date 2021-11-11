from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', id='username', validators=[
                           DataRequired()], render_kw={'placeholder': 'leonards'})
    password = PasswordField('Password', id='password', validators=[
                             DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')


class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username',
                           validators=[DataRequired()], render_kw={'placeholder': 'JohnDoe68'})
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()], render_kw={'placeholder': 'johndoe@base.com'})
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()], render_kw={'placeholder': 'Your secret password'})
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[
                                     DataRequired(), EqualTo('password', message='Confirmation password must match password')], render_kw={'placeholder': 'Must match password'})
    submit = SubmitField('Register')


class PostForm(FlaskForm):
    title = StringField('Title', id='title', validators=[DataRequired()])
    content = TextAreaField('Content', id='content',
                            validators=[DataRequired()])
    tag = StringField('Tag', id='tag')
    submit = SubmitField('Create Post')


class EditProfile(FlaskForm):
    name = StringField('Name', id='name')
    username = StringField('Username', id='username', validators=[
                           DataRequired()], render_kw={'placeholder': 'JohnDoe68'})
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()], render_kw={'placeholder': 'johndoe@base.com'})
    submit = SubmitField('Save Changes')
    
class ReplyForm(FlaskForm):
    slug = HiddenField('Slug', id='slug', validators=[DataRequired()])
    content = TextAreaField('Leave a comment here.',
                            id='content', validators=[DataRequired()])
    reply = SubmitField('Reply')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()], render_kw={'placeholder': 'Your secret password'})
    new_password = PasswordField('Password', id='new_password',
                             validators=[DataRequired()], render_kw={'placeholder': 'Your secret password'})
    confirm_new_password = PasswordField('Confirm Password', id='confirm_new_password', validators=[
                                     DataRequired(), EqualTo('new_password', message='Confirmation password must match password')], render_kw={'placeholder': 'Must match password'})
    submit = SubmitField('Save Changes')
