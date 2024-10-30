
from http import HTTPStatus
from http.client import HTTPException
from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from src.models.models import User
from src.service import generatorNameService
from src.service.security import get_current_user

router = APIRouter(prefix='/names-generator', tags=['names'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get('/get-names', status_code=HTTPStatus.OK)
async def generateNames( current_user: Annotated[User, Depends(get_current_user)],):
    try:
        return await generatorNameService.callGenerateName()

    except:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='error find names ',
        )
