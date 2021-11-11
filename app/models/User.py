from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, DateTime,Text

from app import db


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