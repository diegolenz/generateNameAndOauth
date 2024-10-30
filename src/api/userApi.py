from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from src.models.models import CreateUserRequestDto
from src.service import userRepositoryFake
from src.service.security import get_password_hash

router = APIRouter(prefix='/users', tags=['users'])
#Session = Annotated[Session, Depends(get_session)]
#CurrentUser = Annotated[User, Depends(get_current_user)]



#async def generateNames(token: str = Depends(oauth2_scheme)):
@router.get('/get-user', status_code=HTTPStatus.OK)
async def getUser():
    return await userRepositoryFake.getUserById("1")


@router.post('/', status_code=HTTPStatus.CREATED)
async def create_user(user: CreateUserRequestDto):
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

    await userRepositoryFake.create(db_user)

    return
