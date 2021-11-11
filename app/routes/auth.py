import re
from flask import Blueprint, render_template, request, session
from flask.helpers import flash, make_response, url_for
from werkzeug.utils import redirect
from flask_login import login_required, logout_user, current_user

from app.forms import LoginForm, CreateAccountForm, EditProfile
from app.controllers.AuthController import AuthController

auth = Blueprint('auth', __name__)
auth_controller = AuthController()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.authenticate(request.form)
            return redirect(url_for('forum.index'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    if current_user.is_authenticated:
        return redirect(url_for('forum.index'))
    view = render_template('pages/login.html', form=form)
    return make_response(view)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = CreateAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            auth_controller.create_user(request)
            flash('Register successful, please login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    if current_user.is_authenticated:
        return redirect(url_for('forum.index'))
    view = render_template('pages/register.html', form=form)
    return make_response(view)


@login_required
@auth.route('/my-profile', methods=['GET'])
def my_profile():
    view = render_template('pages/profile.html', user=current_user)
    return make_response(view)


@login_required
@auth.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfile(obj=current_user)
    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.edit_profile(request.form)
            flash('Profile edited', 'success')
        except Exception as e:
            flash(f'{e}', 'danger')
    view = render_template('pages/edit_profile.html', form=form)
    return make_response(view)


@auth.route('/u/<string:username>', methods=['GET'])
def profile(username=None):
    try:
        user = auth_controller.get_user(username)
    except Exception as e:
        flash(f'{e}', 'danger')
        return redirect(url_for('forum.index'))

    view = render_template('pages/profile.html', user=user, posts=user.posts)
    return make_response(view)


@login_required
@auth.route('/update-password', methods=['GET', 'POST'])
def update_password():
    form = EditProfile()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.update_password(request.form)
            flash(f'Password updated', 'success')
        except Exception as e:
            flash(f'{e}', 'danger')

    view = render_template('update_password.html', form=form)
    return make_response(view)


@login_required
@auth.route('/delete-account',  methods=['POST'])
def delete_account():
    try:
        auth_controller.delete_account()
        redirect('auth.logout')
    except Exception as e:
        flash(f'{e}', 'danger')
    return redirect(url_for('base.index'))


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base.index'))
