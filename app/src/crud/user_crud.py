from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.src.models.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, username: str, email: str, password: str):
    new_user = User(username=username, email=email, password_hash=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
