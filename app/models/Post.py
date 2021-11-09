from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, DateTime, Text


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(64), nullable=False)
    body = Column(Text, nullable=False)
    # title separated by dash, and id ex: this-is-title-1628349812219
    slug = Column(Text, nullable=False)
    # slug operations
    # replace space on title with dash
    # add uuidv1 and generate the hex version
    tag = Column(String(32), nullable=True)
    vote = Column(Integer, default=0)
    replies = relationship('Reply', backref='post', lazy=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
