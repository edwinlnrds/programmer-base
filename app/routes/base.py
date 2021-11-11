from flask import Blueprint, render_template, make_response, redirect, url_for
from flask_login import current_user

base = Blueprint('base', __name__)


@base.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('forum.index'))
    view = render_template('pages/index.html')
    return make_response(view)