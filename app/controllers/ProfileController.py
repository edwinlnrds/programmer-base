from datetime import timedelta

from app import db
from app.models.User import User
from flask import flash
from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash


class ProfileController:
    def edit_profile(self, form):
        username = form['username']
        name = form['name']
        email = form['email']

        id = current_user.id
        if current_user.username != username:
            user = User.get(current_user.username)
            if user:  # check if username exists
                raise Exception('Username already used!')

        if current_user.email != email:
            user = User.get(email=email)
            if user:  # check if email exists
                raise Exception('Email already used!')
        user = User.get(id=id)
        user.name = name
        user.username = username
        user.avatar_url = f'https://avatars.dicebear.com/api/initials/{user.username}.svg'
        user.email = email

        db.session.commit()

    def update_password(self, form):
        '''
        Fungsi untuk memperbaharui password
        '''
        user = User.get(current_user.username)
        password = form['password']
        new_password = form['new_password']
        confirm_new_password = form['confirm_new_password']

        # Mengecek apakah password sesuai
        if not check_password_hash(user.password, password):
            # Jika tidak maka beri alert password salah
            raise Exception('Wrong Password')

        if confirm_new_password != new_password:
            raise Exception(
                'Confirm password does not match with new password')

        user.password = generate_password_hash(new_password)
        db.session.commit()

    def delete_account(self):
        db.session.delete(current_user)
        db.session.commit()
        flash(f'Account deleted', 'success')
