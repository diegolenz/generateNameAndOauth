from http import HTTPStatus


from src.api import generatorNameApi
from src.api import users
from src.api import auth
from fastapi import FastAPI


from src.config.settings import get_settings

app = FastAPI()

app.include_router(users.router)
app.include_router(generatorNameApi.router)
app.include_router(auth.router)
# app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}



