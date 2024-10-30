from http import HTTPStatus


from src.api import generatorNameApi
from src.api import userApi
from src.api import authApi
from fastapi import FastAPI




app = FastAPI()

app.include_router(userApi.router)
app.include_router(generatorNameApi.router)
app.include_router(authApi.router)
# app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}



