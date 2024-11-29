from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    bio = Column(Text, nullable=True)
    profile_picture = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    articles = relationship("Article", back_populates="owner")


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


class Calculation(Base):
    __tablename__ = 'calculations'
    calc_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'))
    calculation_type = Column(String(50), nullable=False)
    parameters = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


class Graph(Base):
    __tablename__ = 'graphs'
    graph_id = Column(Integer, primary_key=True, index=True)
    calc_id = Column(Integer, ForeignKey('calculations.calc_id', ondelete='CASCADE'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
