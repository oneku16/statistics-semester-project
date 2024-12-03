from pydantic import BaseModel
from typing import Optional


class ArticleBase(BaseModel):
    title: Optional[str] = None
    content: str
    is_public: bool = False

class ArticleCreate(ArticleBase):
    pass

class CommentBase(BaseModel):
    content: str
