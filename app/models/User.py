from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime

from app import db


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    username = Column(String(64), nullable=False, unique=True)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
