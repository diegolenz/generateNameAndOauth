from logging import exception

import requests

ApiUrlNameMock = 'https://63222793fd698dfa290810b6.mockapi.io/api/nameCreator';

async def callGenerateName():
    response = requests.get(ApiUrlNameMock)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro na requisição: {response.status}")
        raise exception("Erro ao buscar nomes")

