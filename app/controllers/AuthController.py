from datetime import timedelta
from flask import session, flash
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.User import User


class AuthController:
    """  """
    def __init__(self):
        self.user = User()

    def create_user(self, request):
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password: # Assert if both contains the same password
            raise Exception('Confirmation Password does not match Password')

        user = User.query.filter_by(username=username).first()
        if user:  # check if username exists
            raise Exception('Username already used!')

        user = user.query.filter_by(email=email).first()
        if user:  # check if email exists
            raise Exception('Email already used!')

        user = User()
        user.username = username
        user.email = email
        user.password = generate_password_hash(request.form['password'])
        db.session.add(user)
        db.session.commit()

    def authenticate(self, request):
        username = request.form['username']
        password = request.form['password']
        remember = request.form['remember']

        user = User.query.filter_by(username=username).first()

        if not user:
            raise Exception('Username or Password is invalid!')

        if not check_password_hash(user.password, password):
            raise Exception('Username or Password is invalid!')

        login_user(user, remember=remember, duration=timedelta(days=15))

        flash(f'Welcome {user.username}!')
        session['username'] = user.username
        session['name'] = user.name
        session['logged_in'] = True
        session.permanent = False

    def update_password(self, request):
        password = request.form['password']
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if confirm_new_password != new_password:
            raise Exception('Confirm password does not match with new password')
        

    def edit_profile(self,user_id, request):
        pass