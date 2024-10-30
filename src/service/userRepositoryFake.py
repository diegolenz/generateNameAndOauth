from datetime import datetime

import aiohttp
from collections import namedtuple

import requests

from src.models.models import User, CreateUserRequestDto
import json
import asyncio

ApiUrlNameMock = 'https://63222793fd698dfa290810b6.mockapi.io/api/users'

async def getUserById(id):
    print(id)
    async with aiohttp.ClientSession() as session:
        async with session.get(ApiUrlNameMock + "/" + id ) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
                jsonDump = json.dumps(data)
                print(jsonDump)
                loadJson = json.loads(jsonDump)
                print(loadJson)
                user = User(**loadJson)
                print(user)
                return user
            else:
                print(f"Erro na requisição: {response.status}")
    return None

#Mock usado não consigo colocar para buscar pelo campo que não seja id (Não é escalavel) - é limitado na versão free
async def findByUser(userName: str ):
    print(userName)
    async with aiohttp.ClientSession() as session:
        async with session.get(ApiUrlNameMock) as response:
            if response.status == 200:
                data = await response.json()

                listU = list()
                for item in data:
                    u = User(item['id'], item['password'], item['email'], item['userName'], item['createdAt'])
                    listU.append(u)


                return next(filter(lambda us: us.userName == userName, listU), None)
            else:
                print(f"Erro na requisição: {response.status}")
    return None

#Mock usado não consigo colocar para buscar pelo campo que não seja id - é limitado na versão free
async def create(user: CreateUserRequestDto ):
    #user.createdAt = datetime.now()
    #print(f"Nome: {user.userName}, email: {user.email}, created: {user.createdAt}, pass: {user.password}, id{user.id}")
    jsonstr1 = json.dumps(user.__dict__)
    print(jsonstr1)
    response = requests.post(ApiUrlNameMock,  data= jsonstr1)
    print(response)
    if response.status_code  != 200:
        raise Exception("Falha ao inserir usuario")
    #async with aiohttp.ClientSession() as session:
    #    async with session.post(ApiUrlNameMock, json = user.toJSON()) as response:




def getUserByIdSync(id):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(getUserById(id))
