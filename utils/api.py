import asyncio

from pyonlinesim import OnlineSMS
api_token = '5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67'
async def get_balance() -> None:
    async with OnlineSMS(api_token) as client:
        result = await client.get_balance()  # Balance(response='1', balance=0.0, frozen_balance=0.0)
        return result
# asyncio.run(get_balance(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88'))


# res = asyncio.run(get_balance(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88'))
# async def save_service(api_token: str, country: str) -> None:
#     country = "russia"
#     async with OnlineSMS(api_token) as client:
#         country = await client.get_services(country=country)
#         for service in country.services:
# #             # print(f'ID: {service.id} | Available Numbers: {service.count} | Service: {service.service} | Price: {service.price}')

