from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.models.models import CreateUserRequestDto, User
from src.service import userRepositoryFake
from src.service.security import get_password_hash, oauth2_scheme
from typing import Annotated
from src.service.security import get_current_user


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', status_code=HTTPStatus.CREATED)
async def create_user(user: CreateUserRequestDto, current_user: Annotated[User, Depends(get_current_user)]):
    db_user = await userRepositoryFake.findByUser(user.userName)

    if db_user:
        if db_user.userName == user.userName:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    hashed_password = get_password_hash(user.password)
    print(hashed_password)

    db_user = CreateUserRequestDto(
        password= hashed_password,
        email = user.email,
        userName = user.userName
    )

    try:
        await userRepositoryFake.create(db_user)
        return HTTPException(
            status_code=HTTPStatus.CREATED,
            detail='created user',
        )
    except:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='create user error ',
        )