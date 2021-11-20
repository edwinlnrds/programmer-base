from datetime import timedelta

from app import db
from app.models.User import User
from flask import flash, session
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash


class AuthController:
    """  
    Controller yang mengelola otentikasi 

    """

    def check_username_and_email(self, username, email):
        ''''
        Fungsi untuk mengecek apakah usernam atau email sudah digunakan
        '''
        user = User.get(username)
        if user:  # check if username exists
            raise Exception('Username already used!')

        user = User.get(email=email)
        if user:  # check if email exists
            raise Exception('Email already used!')

    def create_user(self, form):
        ''''
        Fungsi untuk membuat user/akun baru
        '''
        email = form['email']
        username = form['username']
        password = form['password']
        confirm_password = form['confirm_password']

        if password != confirm_password:  # Assert if both contains the same password
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
        '''
        Fungsi untuk otentikasi/login
        '''
        username = form['username']
        password = form['password']

        user = User.get(username)
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
