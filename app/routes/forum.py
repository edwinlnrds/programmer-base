from flask import Blueprint, render_template, request
from flask_login import login_required

forum = Blueprint('forum', __name__)

@forum.route('/', methods=['GET'])
def index():
    pass

@forum.route('/<string:slug>')
def post_detail():
    pass

@login_required
@forum.route('/create')
def create_post():
    pass

@login_required
@forum.route('/edit')
def edit_post():
    pass

@login_required
@forum.route('/delete/<int:id>')
def delete_post():
    pass

@forum.route('/reply')
@login_required
def reply_to_post():
    pass