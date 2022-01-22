from app.controllers.ProfileController import ProfileController
from app.forms import ChangePasswordForm, EditProfile
from app.models.User import User
from flask import (Blueprint, abort, flash, make_response, redirect,
                   render_template, request, url_for)
from flask_login import current_user, login_required

profile = Blueprint('profile', __name__)
profile_controller = ProfileController()


@profile.route('/<string:username>', methods=['GET'])
def details(username=None):
    try:
        user = User.get(username)
    except Exception as e:
        flash(f'{e}', 'danger')
        return redirect(url_for('forum.index'))

    view = render_template('pages/profile.html', user=user)
    return make_response(view)


@login_required
@profile.route('/<string:username>/edit', methods=['GET', 'POST'])
def edit(username):
    if current_user.username != username:
        abort(401)  # Unauthorized

    form = EditProfile(request.form, obj=current_user)
    # Jika methode POST dan form validasi saat submit
    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.edit_profile(request.form)
            flash('Profile edited', 'success')
        except Exception as e:
            flash(f'{e}', 'danger')
    view = render_template('pages/edit_profile.html', form=form)
    return make_response(view)


@login_required
@profile.route('/change-password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    # Jika methode POST dan form validasi saat submit
    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.update_password(request.form)
            flash(f'Password updated', 'success')
        except Exception as e:
            flash(f'{e}', 'danger')

    view = render_template('pages/change_password.html', form=form)
    return make_response(view)


@login_required
@profile.route('/delete-account',  methods=['POST'])
def delete_account():
    try:
        profile_controller.delete_account()
        redirect('auth.logout')
    except Exception as e:
        flash(f'{e}', 'danger')
    return redirect(url_for('base.index'))
