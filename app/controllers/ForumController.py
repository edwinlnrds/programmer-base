from flask_login import current_user
from sqlalchemy import desc

from app import db
from app.models.Post import Post
from app.models.Reply import Reply
from app.helpers import convert_to_slug

class ForumController:
    """
    Controller yang mengelola seluruh kegiatan dan aktivitas
    yang berhubungan dengan forum termasuk membuat post, membalas post (reply),
    ataupun menghapus, mengubah atau mengambil data post, reply dari database
    """
    def create_post(self, form):
        """
        Fungsi untuk membuat post
        """
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

    def edit_post(self, post, form):
        """
        Fungsi untuk meng-edit post
        """
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
        """
        Fungsi untuk menghapus post
        """
        post = self.get_post(slug=slug)
        replies = post.replies

        # sebelum menghapus post
        # menghapus balasan terlebih dahulu
        for reply in replies:
            db.session.delete(reply)
        db.session.delete(post)
        db.session.commit()

    def get_reply(self, id):
        return Reply.query.filter_by(id=id).first()

    def reply_to_post(self, form):
        """
        Fungsi untuk membuat balasan ke sebuah post
        """
        slug = form['slug']
        post_id = self.get_post(slug).id
        reply = Reply(
            user_id=current_user.id,
            post_id=post_id,
            content=form['content'])

        db.session.add(reply)
        db.session.commit()
    
    def edit_reply(self, form):
        """
        Fungsi untuk mengedit balasan
        """
        id = form['id']

        reply = self.get_reply(id)
        reply.content = form['content']
        db.session.commit()

    def delete_reply(self, form):
        """
        Fungsi untuk menghapus balasan
        """
        reply = self.get_reply(form['id'])
        db.session.delete(reply)
        db.session.commit()