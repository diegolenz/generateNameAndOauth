import aiohttp


ApiUrlNameMock = 'https://63222793fd698dfa290810b6.mockapi.io/api/nameCreator';

async def callGenerateName():
    async with aiohttp.ClientSession() as session:
        async with session.get(ApiUrlNameMock) as response:
            if response.status == 200:
                data = await response.json()
                print(f"a: {response}")
                print(f"b: {data}")
                return data
            else:
                print(f"Erro na requisição: {response.status}")
    return None

