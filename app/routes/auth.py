from app.controllers.AuthController import AuthController
from app.forms import CreateAccountForm, LoginForm
from flask import Blueprint, render_template, request
from flask.helpers import flash, make_response, url_for
from flask_login import current_user, login_required, logout_user
from werkzeug.utils import redirect

# Blueprint merupakan komponen modular untuk menampung route
auth = Blueprint('auth', __name__)
auth_controller = AuthController()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    # Jika methode POST dan form validasi saat submit
    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.authenticate(request.form)
            return redirect(url_for('forum.index'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)
    # Jika user sudah login
    if current_user.is_authenticated:
        # arahkan ke forum
        return redirect(url_for('forum.index'))
    view = render_template('pages/login.html', form=form)
    return make_response(view)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = CreateAccountForm(request.form)

    # Jika methode POST dan form validasi saat submit
    if request.method == 'POST' and form.validate():
        try:
            auth_controller.create_user(request.form)
            flash('Register successful, please login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    # Jika user sudah login
    if current_user.is_authenticated:
        # arahkan ke forum
        return redirect(url_for('forum.index'))
    view = render_template('pages/register.html', form=form)
    return make_response(view)


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base.index'))
