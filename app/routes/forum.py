from datetime import datetime

from app.controllers.ForumController import ForumController
from app.forms import PostForm, ReplyForm
from flask import (Blueprint, abort, flash, make_response, render_template,
                   request)
from flask.helpers import url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

forum = Blueprint('forum', __name__)
forum_controller = ForumController()


@forum.route('/', methods=['GET'])
def index():
    page = request.args.get('page') if request.args.get('page') else 1
    posts = forum_controller.get_post(page)
    view = render_template('pages/posts.html', user=current_user, posts=posts)
    return make_response(view)


@forum.route('/<string:slug>')
def post_detail(slug):
    post = forum_controller.get_post(slug=slug)
    form = ReplyForm(slug=slug)
    if not post:
        abort(404)
    view = render_template('pages/post_detail.html',
                           post=post,
                           replies=post.replies,
                           form=form)
    return make_response(view)


@login_required
@forum.route('/create', methods=['GET', 'POST'])
def create_post():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    form = PostForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            forum_controller.create_post(request.form)
            return redirect(url_for('forum.index'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    view = render_template('pages/create_edit.html',
                           form=form,
                           action=url_for('forum.create_post'),
                           operation='Create')
    return make_response(view)


@login_required
@forum.route('/<string:slug>/edit', methods=['GET', 'POST'])
def edit_post(slug):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    post = forum_controller.get_post(slug=slug)
    if not post:
        abort(404)

    form = PostForm(obj=post)
    form.submit.label.text = 'Save Changes'
    if request.method == 'POST' and form.validate_on_submit():
        try:
            slug = forum_controller.edit_post(post, request.form)
            return redirect(url_for('forum.post_detail', slug=slug))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    view = render_template('pages/create_edit.html', form=form,
                           post=post,
                           action=url_for('forum.edit_post',
                                          slug=post.slug),
                           operation='Edit')
    return make_response(view)


@login_required
@forum.route('/<string:slug>/delete', methods=['POST'])
def delete_post(slug):
    try:
        forum_controller.delete_post(slug)
        flash(f'Post deleted', 'success')
        return redirect(url_for('forum.index'))
    except Exception as e:
        flash(f'{e}', 'danger')
        return redirect(request.referrer)


@login_required
@forum.route('/reply', methods=['POST'])
def create_reply():
    try:
        forum_controller.reply_to_post(request.form)
        flash('Reply success', 'success')
        return redirect(url_for('forum.post_detail', slug=request.form['slug']))
    except Exception as e:
        flash(f'{e}', 'danger')
        return redirect(request.referrer)


@login_required
@forum.route('/reply/edit', methods=['POST'])
def edit_reply():
    try:
        forum_controller.edit_reply(request.form)
        flash(f'Reply edited', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(request.referrer)


@login_required
@forum.route('/reply/delete', methods=['POST'])
def delete_reply():
    try:
        forum_controller.delete_reply(request.form)
        flash(f'Reply deleted', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(request.referrer)
