from sqlalchemy.orm import Session

from ..models.article import Article


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
