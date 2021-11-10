from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column
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
