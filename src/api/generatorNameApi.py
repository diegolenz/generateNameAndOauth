
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from src.service import generatorNameService

router = APIRouter(prefix='/names-generator', tags=['names'])
# Session = Annotated[Session, Depends(get_session)]
# CurrentUser = Annotated[User, Depends(get_current_user)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get('/get-names', status_code=HTTPStatus.OK)
#async def generateNames(token: str = Depends(oauth2_scheme)): #com autorização
async def generateNames():
    return await generatorNameService.callGenerateName()