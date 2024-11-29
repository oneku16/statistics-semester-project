from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Article, Comment

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.user_id == user_id))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user: User):
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def create_article(db: AsyncSession, article: Article):
    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article

async def create_comment(db: AsyncSession, comment: Comment):
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment
