from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from src.models.models import User, Token
from src.service.security import (
    create_access_token,
    get_current_user,
    verify_password,
)
from src.service import userRepositoryFake
router = APIRouter(prefix='/auth', tags=['auth'])

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#Session = Annotated[Session, Depends(get_session)]


@router.post('/token', response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()] ):
    print(form_data.username)
    user = await userRepositoryFake.findByUser(form_data.username)

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh_token', response_model=Token)
def refresh_access_token(
    user: User = Depends(get_current_user),
):
    new_access_token = create_access_token(data={'sub': user.email})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
