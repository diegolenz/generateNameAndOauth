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


#Mock usado não consigo colocar para buscar pelo campo que não seja id (Não é escalavel) - é limitado na versão free
async def findByEmail(email: str ):
    async with aiohttp.ClientSession() as session:
        async with session.get(ApiUrlNameMock) as response:
            if response.status == 200:
                data = await response.json()

                listU = list()
                for item in data:
                    u = User(item['id'], item['password'], item['email'], item['userName'], item['createdAt'])
                    listU.append(u)


                return next(filter(lambda us: us.email == email, listU), None)
            else:
                print(f"Erro na requisição: {response.status}")
    return None

async def create(user: CreateUserRequestDto ):
    user.createdAt = "2024-10-29T19:13:49.999Z";
    jsonstr1 = json.dumps(user.__dict__)
    print(jsonstr1)
    headers = {
        "Content-Type": "application/json"  # Se estiver enviando JSON
    }
    response = requests.post(ApiUrlNameMock,  data=jsonstr1, headers=headers)
    if response.status_code  != 201:
        raise Exception("Falha ao inserir usuario ")




def getUserByIdSync(id):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(getUserById(id))
