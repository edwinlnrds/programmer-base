import re
from flask import Blueprint, render_template, request, session
from flask.helpers import flash, make_response, url_for
from werkzeug.utils import redirect
from flask_login import login_required, logout_user, current_user

from app.forms import LoginForm, CreateAccountForm
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
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    if current_user.is_authenticated:
        return redirect(url_for('forum.index'))
    view = render_template('pages/register.html', form=form)
    return make_response(view)


@login_required
@auth.route('/my-profile')
def my_profile():
    view = render_template('pages/profile.html')
    return make_response(view)

@login_required
@auth.route('/edit-profile')
def edit_profile():
    pass

@auth.route('/u/<int:id>')
def profile():
    pass

@login_required
@auth.route('/update-password')
def update_password():
    try:
        auth_controller.update_password(request)
    except Exception as e:
        flash(f'{e}', 'danger')


@login_required
@auth.route('/delete-account')
def delete_account():
    return redirect(url_for('base.index'))


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')
