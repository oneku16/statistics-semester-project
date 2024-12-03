from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database import Base


class Article(Base):
    __tablename__ = 'articles'
    article_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'))
    title = Column(String(200), nullable=True)
    content = Column(Text, nullable=False)
    is_public = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="articles")
    comments = relationship("Comment", back_populates="article")


class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('articles.article_id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'))
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    article = relationship("Article", back_populates="comments")
