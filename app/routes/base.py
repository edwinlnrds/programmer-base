from flask import Blueprint, render_template, make_response

base = Blueprint('base', __name__)


@base.route('/')
def index():
    view = render_template('pages/index.html', title='Home')
    return make_response(view)