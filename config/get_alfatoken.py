import aiohttp
import asyncio
import json
from config.cf import alfa_token

# Получение токена
async def get_token_from_alfa(email):
    url = 'https://testkiberone.s20.online/v2api/auth/login'
    data = {'email': email, 'api_key': alfa_token}

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status != 200:
                result = await response.json()
                raise Exception(f"{result['name']} - {result['message']}")
            result = await response.json()
            return result['token']

async def get_token():
    try:
        # Возвращаем токен
        return await get_token()
    except Exception as e:
        print(f"Ошибка: {str(e)}")


