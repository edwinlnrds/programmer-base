from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Text

import uuid

from app import db


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)
    tag = Column(String(32), nullable=True)
    vote = Column(Integer, default=0, nullable=True)
    # has_voted = Column()
    replies = relationship('Reply')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def get_created_at(self):
        return self.created_at.strftime("%H:%m, %B %d %Y")