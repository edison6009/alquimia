from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: Optional[EmailStr] = None

    model_config = ConfigDict(str_strip_whitespace=True)