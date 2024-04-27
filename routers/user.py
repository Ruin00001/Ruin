from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from starlette import status
from cruds import user as user_cruds
from schemas import UserCreate, UserResponse


# DbDependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", status_code=status.HTTP_200_OK)
async def find_all():
    return user_cruds.find_all()

@router.post("/", status_code=status.HTTP_200_OK)
async def create_by_name(user_create=Body()):
    print('====')
    print(user_create)
    return user_cruds.create(user_create)

