from datetime import datetime

from app import db
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    avatar_url = Column(Text, nullable=True)
    name = Column(String(255), nullable=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    posts = relationship('Post')

    def get_created_at(self):
        return self.created_at.strftime("%B %d %Y")

    @staticmethod
    def get(username=None, email=None, id=None):
        '''
        Fungsi untuk mengambil data pengguna dari database
        '''
        if username:
            return User.query.filter_by(username=username).first()
        
        if email:
            return User.query.filter_by(email=email).first()

        if id:
            return User.query.filter_by(id=id).first()

        
