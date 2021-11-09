from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Integer, DateTime, Text

from app import db


class Reply(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    vote = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
