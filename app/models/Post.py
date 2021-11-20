from datetime import datetime

from app import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DateTime, Integer, String, Text


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    # merupakan campuran dari judul dan uuid sebagai alamat untuk
    # mengakses post, hal ini dilakukan untuk menghindari penggunaan id
    # yang mudah ditebak
    slug = Column(Text, nullable=False)
    tag = Column(String(32), nullable=True)
    vote = Column(Integer, default=0, nullable=True)
    replies = relationship('Reply')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def get_created_at(self):
        import pytz  # $ pip install pytz
        # Untuk mengambil local timezone
        import tzlocal  # $ pip install tzlocal

        local_timezone = tzlocal.get_localzone()  # get pytz tzinfo
        local_time = self.created_at.replace(
            tzinfo=pytz.utc).astimezone(local_timezone)
        return local_time.strftime("%H:%M, %B %d %Y")
