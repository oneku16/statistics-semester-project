from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str

class ArticleBase(BaseModel):
    title: Optional[str] = None
    content: str
    is_public: bool = False

class ArticleCreate(ArticleBase):
    pass

class CommentBase(BaseModel):
    content: str

class CalculationBase(BaseModel):
    calculation_type: str
    parameters: dict
    result: dict
