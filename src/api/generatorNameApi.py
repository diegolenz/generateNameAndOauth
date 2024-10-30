
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from src.service import generatorNameService

router = APIRouter(prefix='/names-generator', tags=['names'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get('/get-names', status_code=HTTPStatus.OK)
async def generateNames(token: str = Depends(oauth2_scheme)):
    return await generatorNameService.callGenerateName()