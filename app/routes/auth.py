from flask import Blueprint, render_template, request, session
from flask.helpers import flash, make_response, url_for
from werkzeug.utils import redirect
from flask_login import login_required, logout_user

from app.auth.forms import LoginForm, CreateAccountForm
from app.controllers.AuthController import AuthController

auth = Blueprint('auth', __name__)
auth_controller = AuthController()


@auth.route('/', methods=['POST'])
def authenticate(): 
    try:
        auth_controller.authenticate(request=request)
        return redirect(url_for('base'))
    except Exception as e:
        flash(f'{e}', 'danger')
        return redirect(request.referrer)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    view = render_template('pages/login.html', title='Login', form=form)
    return make_response(view)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = CreateAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        auth_controller.create_user(request)
        return redirect(url_for('auth.login'))
    else:
        view = render_template(
            'pages/register.html', title='Register', form=form)
        return make_response(view)


@login_required
@auth.route('/edit-profile')
def edit_profile():
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
    pass


@login_required
def logout():
    logout_user()
