from datetime import datetime, date, time
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Text

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
        import pytz    # $ pip install pytz
        # Untuk mengambil local timezone
        import tzlocal # $ pip install tzlocal

        local_timezone = tzlocal.get_localzone() # get pytz tzinfo
        local_time = self.created_at.replace(tzinfo=pytz.utc).astimezone(local_timezone)
        return local_time.strftime("%H:%m, %B %d %Y")