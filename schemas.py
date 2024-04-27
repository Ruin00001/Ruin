from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict



class UserCreate(BaseModel):
    user_name: str = Field(min_length=2, max_length=20, examples=["PC"])
    status: str


class UserResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    user_name: str = Field(min_length=2, max_length=20, examples=["PC"])
    status: bool
    updated_at: datetime

    #model_config = ConfigDict(from_attributes=True)

