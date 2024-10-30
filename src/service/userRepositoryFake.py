from datetime import datetime

import aiohttp

import requests
from src.models.models import User, CreateUserRequestDto
import json

ApiUrlNameMock = 'https://63222793fd698dfa290810b6.mockapi.io/api/users'

#Mock usado não consigo colocar para buscar pelo campo que não seja id (Não é escalavel) - é limitado na versão free
async def findByUser(userName: str ):
    response = requests.get(ApiUrlNameMock)
    if response.status_code == 200:
        data = response.json()

        listUsers = list()
        for itemUser in data:
            user = User(itemUser['id'], itemUser['password'], itemUser['email'], itemUser['userName'],
                        itemUser['createdAt'])
            listUsers.append(user)

        return next(filter(lambda us: us.userName == userName, listUsers), None)

    else:
        raise Exception(f"Error find by user {response.status}")



#Mock usado não consigo colocar para buscar pelo campo que não seja id (Não é escalavel) - é limitado na versão free
async def findByEmail(email: str ):
    response = requests.get(ApiUrlNameMock)
    if response.status_code == 200:
        data = response.json()

        listUsers = list()
        for itemUser in data:
            user = User(itemUser['id'], itemUser['password'], itemUser['email'], itemUser['userName'], itemUser['createdAt'])
            listUsers.append(user)

        return next(filter(lambda us: us.email == email, listUsers), None)

    else:
        raise Exception(f"Error find by user email {response.status}")


async def create(user: CreateUserRequestDto ):
    #user.createdAt = "2024-10-29T19:13:49.999Z";
    jsonBody = json.dumps(user.__dict__)

    headers = {
        "Content-Type": "application/json"  # Se estiver enviando JSON
    }
    response = requests.post(ApiUrlNameMock,  data=jsonBody, headers=headers)

    if response.status_code != 201:
        raise Exception("Error insert user ")


