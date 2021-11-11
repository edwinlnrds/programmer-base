from datetime import timedelta
from flask import session, flash
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.User import User


class AuthController:
    """  """
    def check_username_and_email(self, username, email):
        user = self.get_user(username)
        if user:  # check if username exists
            raise Exception('Username already used!')

        user = self.get_user(email=email)
        if user:  # check if email exists
            raise Exception('Email already used!')


    def create_user(self, form):
        email = form['email']
        username = form['username']
        password = form['password']
        confirm_password = form['confirm_password']

        if password != confirm_password: # Assert if both contains the same password
            raise Exception('Confirmation Password does not match Password')

        self.check_username_and_email(username, email)

        user = User()
        user.username = username
        user.email = email
        user.avatar_url = f'https://avatars.dicebear.com/api/initials/{username}.svg'
        user.password = generate_password_hash(form['password'])
        db.session.add(user)
        db.session.commit()

    def authenticate(self, form):
        username = form['username'] 
        password = form['password']
        # remember = form['remember']

        user = self.get_user(username)
        if not user:
            raise Exception('Username or Password is invalid!')

        if not check_password_hash(user.password, password):
            raise Exception('Username or Password is invalid!')

        logged_in = login_user(user, duration=timedelta(days=3))

        if logged_in:
            flash(f'Welcome {user.username}!', 'success')
            session['username'] = user.username
            session['name'] = user.name
            session['logged_in'] = True
            session.permanent = False

    def update_password(self, form):
        user = self.get_user(current_user.username)
        password = form['password']
        new_password = form['new_password']
        confirm_new_password = form['confirm_new_password']

        if not check_password_hash(user.password, password):
            raise Exception('Wrong Password')

        if confirm_new_password != new_password:
            raise Exception('Confirm password does not match with new password')
        
        user.password = generate_password_hash(new_password)
        db.session.commit()

        
    def get_user(self, username=None, email=None, id=None):        
        if username:
            return User.query.filter_by(username=username).first()
        if email:
            return User.query.filter_by(email=email).first()
        if id:
            return User.query.filter_by(id=id).first()
            
    def edit_profile(self, form):
        username = form['username']
        name = form['name']
        email = form['email']

        id = current_user.id
        if current_user.username != username:
            user = self.get_user(current_user.username)
            if user:  # check if username exists
                raise Exception('Username already used!')

        if current_user.email != email:
            user = self.get_user(email=email)
            if user:  # check if email exists
                raise Exception('Email already used!')
        user = self.get_user(id=id)
        user.name = name
        user.username = username
        user.avatar_url = f'https://avatars.dicebear.com/api/initials/{user.username}.svg'
        user.email = email

        db.session.commit()

    def delete_account(self):
        db.session.delete(current_user)
        db.session.commit()
        flash(f'Account deleted', 'success')