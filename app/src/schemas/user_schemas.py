from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str
