from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database,UserBalanceDB,Channel,BanUser,StateBot,ProductPriceDB,PaymentChecker,SoldNumbers
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="data/main.db")
balance = UserBalanceDB("data/user_balances.db")
price = ProductPriceDB("data/product_prices.db")
paymentchecker = PaymentChecker("data/payment_checker.db")
soldnumbers = SoldNumbers("data/sold_numbers.db")
channels = Channel("data/main.db")
banuser = BanUser("main.db")
botstate = StateBot("data/main.db")

# soldnumbers.save_number(user_id="1002468249",data=f"uzbekistan:instagram:479895",number="+998904050006547")
# all_users = soldnumbers.get_numbers(user_id=call.from_user.id)

# import asyncio

# from pyonlinesim import OnlineSMS
# from utils.get_number import get_country
# import requests

# def dollar_to_rub(amount_in_dollar):
#     url = "https://api.exchangerate-api.com/v4/latest/USD"
#     response = requests.get(url)
#     data = response.json()
    
#     if response.status_code == 200:
#         rub_rate = data['rates']['RUB']
#         amount_in_rub = amount_in_dollar * rub_rate
#         return amount_in_rub
#     else:
#         return 20
# country = ["africa","venezuela","congo","egypt","philippens","hongkong","romania","singapore","tobago","china","switzerland","slovakia","moldova","korea","spain","morocco","bangladesh","pakistan","germany","qatar","portugal","sweden","canada","bahrain","kuwait","italy"]
# services = ["amazon","discord","Авито","СБЕР (Маркет, Мегамаркет, Здоровье и др) не СберID","tinder","instagram","facebook", "microsoft","apple","steam","telegram","uber","twitter","whatsapp","яндекс","tiktok (тикток)","Google","twitter","eBay|Kleinanzeigen.","вконтакте"]

# async def get_services(api_token: str, countries: str, service_: str) -> None:

#     async with OnlineSMS(api_token) as client:
#         for country_ in countries:
#             try:
#                 country = await client.get_services(country=get_country(country_))
#                 for service_ in services:
#                     for service in country.services:
#                         if service_.capitalize().startswith(service.service) or service.service.capitalize().startswith(service_) or service.service.lower() == service_.lower():
#                             if service_ == "Авито":service_ = "avito"
#                             elif service_.startswith("СБЕР"):service_ = "sbermarket"
#                             elif service_ == "яндекс":service_ = "yandex"
#                             elif service_ == "tiktok (тикток)":service_ = "tiktok"
#                             elif service_ == "eBay|Kleinanzeigen.":service_ = "ebay"
#                             elif service_ == "вконтакте":service_ = "vkontakte"
#                             else:pass
#                             price_ = service.price
#                             price_ = dollar_to_rub(float(price_))
#                             price_ = float(price_) + 20 
#                             price_ = round(float(price_)*100)/100       
#                             price.save_price(f'{country_}:{service_}',price_)
#                             print(f"Successfully saved [{country_}:{service_}] ({price_})")
#             except:pass
# if __name__ == '__main__':
#     asyncio.run(get_services(api_token='5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67',countries=country,service_=services))