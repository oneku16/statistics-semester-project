from sqlalchemy.orm import Session
from .models import User, Article


def create_user(db: Session, username: str, email: str, password_hash: str):
    new_user = User(username=username, email=email, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_article(db: Session, user_id: int, title: str, content: str, is_public: bool):
    new_article = Article(user_id=user_id, title=title, content=content, is_public=is_public)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_public_articles(db: Session):
    return db.query(Article).filter(Article.is_public == True).all()

def get_articles_by_user(db: Session, user_id: int):
    return db.query(Article).filter(Article.user_id == user_id).all()
