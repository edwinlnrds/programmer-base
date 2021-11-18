from app import db
from app.helpers import convert_to_slug
from app.models.Post import Post
from app.models.Reply import Reply
from flask_login import current_user
from sqlalchemy import desc


class ForumController:
    def create_post(self, form):
        title = form['title']
        content = form['content']
        tag = form['tag']

        post = Post(
            user_id=current_user.id,
            title=title,
            content=content,
            tag=tag,
            slug=convert_to_slug(title),
        )
        db.session.add(post)
        db.session.commit()

    def get_post(self, slug=None, id=None):
        if slug:
            return Post.query.filter_by(slug=slug).first()
        if id:
            return Post.query.filter_by(id=id).first()

    def get_all(self):
        return Post.query.order_by(desc(Post.created_at)).all()

    def get_post(self, page):
        return Post.query.order_by(desc(Post.created_at)).paginate(page, 10)

    def edit_post(self, post, form):
        title = form['title']
        content = form['content']
        tag = form['tag']

        post.title = title
        post.content = content
        post.tag = tag
        post.slug = convert_to_slug(title)

        db.session.commit()

        return post.slug

    def delete_post(self, slug):
        post = self.get_post(slug=slug)
        replies = post.replies

        for reply in replies:
            db.session.delete(reply)
        db.session.delete(post)
        db.session.commit()

    def get_reply(self, id):
        return Reply.query.filter_by(id=id).first()

    def reply_to_post(self, form):
        slug = form['slug']
        post_id = self.get_post(slug).id
        reply = Reply(
            user_id=current_user.id,
            post_id=post_id,
            content=form['content'])

        db.session.add(reply)
        db.session.commit()

    def edit_reply(self, form):
        id = form['id']

        reply = self.get_reply(id)
        reply.content = form['content']
        db.session.commit()

    def delete_reply(self, form):
        reply = self.get_reply(form['id'])
        db.session.delete(reply)
        db.session.commit()
