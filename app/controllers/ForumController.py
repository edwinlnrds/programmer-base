from flask_login import current_user
from flask import flash

from app import db
from app.models.Post import Post
from app.helpers import convert_to_slug

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
        return Post.query.all()

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
        post = Post.query.filter_by(slug=slug).first()
        db.session.delete(post)
        db.session.commit()