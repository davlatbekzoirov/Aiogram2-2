import asyncio
from pyonlinesim import OnlineSMS
from pyonlinesim.exceptions.sms.order import CantFinishOrder,WrongOperationID,NoNumber,NotEnoughFunds
from pyonlinesim.exceptions.authentication import TryAgainLater


def get__country(nm):
    if nm == "7":
        return "russia"
    if nm == "91":
        return "india"
    if nm == "55":
        return "brazil"
    if nm == "254 ":
        return "kenya"
    if nm == "380":
        return "ukraine"
    if nm == "1":
        return "usa"
    if nm == "33":
        return "france"
    if nm == "51":
        return "peru"
    if nm == "52 ":
        return "mexico"
    if nm == "90":
        return "turkey"
    if nm == "505":
        return "nicagura"
    if nm == "855":
        return "combodia"
    if nm == "66":
        return "thailand"
    if nm == "60":
        return "malaysia"
    if nm == "7":
        return "kazakhstan"
    if nm == "31":
        return "netherlands"
    if nm == "372":
        return "estonia"
    if nm == "996":
        return "kyrgyzstan"
    if nm == "62":
        return "indonesia"
    if nm == "84":
        return "Vietnam"
    if nm == "36":
        return "hungary"
    if nm == "58":
        return "africa"
    if nm == "27":
        return "venezuela"
    if nm == "54":
        return "argentina"
    if nm == "243":
        return "congo"
    if nm == "20":
        return "egypt"
    if nm == "63":
        return "philippens"
    if nm == "852":
        return "hongkong"
    if nm == "40":
        return "romania"
    if nm == "65":
        return "singapore"
    if nm == "868":
        return "tobago"
    if nm == "86":
        return "china"
    if nm == "41":
        return "switzerland" 
    if nm == "421":
        return "slovakia"
    if nm == "373":
        return "moldova"
    if nm == "82":
        return "korea"
    if nm == "34":
        return "spain"
    if nm == "212":
        return "morocco"
    if nm == "880":
        return "bangladesh"
    if nm == "92":
        return "pakistan"
    if nm == "49":
        return "germany"
    if nm == "974":
        return "qatar"
    if nm == "351":
        return "portugal"
    if nm == "46":
        return "sweden"
    if nm == "1":
        return "canada"
    if nm == "973":
        return "bahrain"
    if nm == "965":
        return "kuwait"
    if nm == "39":
        return "italy"
    return "UnKnownCountryError"
def get_country(nm):
    if nm == "russia":
        return 7
    if nm == "india":
        return 91
    if nm == "brazil":
        return 55
    if nm == "kenya":
        return 254
    if nm == "ukraine":
        return 380
    if nm == "usa":
        return 1
    if nm == "france":
        return 33
    if nm == "peru":
        return 51
    if nm == "mexico":
        return 52
    if nm == "turkey":
        return 90
    if nm == "nicagura":
        return 505
    if nm == "combodia":
        return 855
    if nm == "thailand":
        return 66
    if nm == "usa":
        return 1
    if nm == "malaysia":
        return 60
    if nm == "kazakhstan":
        return 7
    if nm == "netherlands":
        return 31
    if nm == "estonia":
        return 372
    if nm == "kyrgyzstan":
        return 996
    if nm == "indonesia":
        return 62
    if nm == "Vietnam":
        return 84
    if nm == "hungary":
        return 36
    if nm == "africa":
        return 27
    if nm == "venezuela":
        return 58
    if nm == "argentina":
        return 54
    if nm == "congo":
        return 243
    if nm == "egypt":
        return 20
    if nm == "philippens":
        return 63
    if nm == "hongkong":
        return 852
    if nm == "romania":
        return 40
    if nm == "singapore":
        return 65
    if nm == "tobago":
        return 868
    if nm == "china":
        return 86
    if nm == "switzerland":
        return 41 
    if nm == "slovakia":
        return 421
    if nm == "moldova":
        return 373
    if nm == "korea":
        return 82
    if nm == "spain":
        return 34
    if nm == "morocco":
        return 212
    if nm == "bangladesh":
        return 880
    if nm == "pakistan":
        return 92
    if nm == "germany":
        return 49
    if nm == "qatar":
        return 974
    if nm == "portugal":
        return 351
    if nm == "sweden":
        return 46
    if nm == "canada":
        return 1
    if nm == "bahrain":
        return 973
    if nm == "kuwait":
        return 965
    if nm == "italy":
        return 39



async def get_price(api_token:str,country: str, service_) -> None:
    async with OnlineSMS(api_token) as client:
        if service_ == "avito":service_ = "Авито"
        elif service_=="sbermarket":service_ = "СБЕР (Маркет, Мегамаркет, Здоровье и др) не СберID"
        elif service_ == "yandex":service_ = "яндекс"
        elif service_ == "tiktok":service_ = "tiktok (тикток)"
        elif service_ == "ebay":service_ = "eBay|Kleinanzeigen."
        elif service_ == "vkontakte":service_ = "вконтакте"
        else:pass
        api_token = '5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67'
        country = await client.get_services(country=country)
        for service in country.services:
            if service_.capitalize().startswith(service.service) or service.service.capitalize().startswith(service_) or service.service.lower() == service_.lower():
                return service.count 

# asyncio.run(get_price(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', service_="telegram",country='380'))


async def finish_order(api_token:str,operation_id: int) -> None:
    try:
        async with OnlineSMS(api_token) as client:
            api_token = '5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67'
            response = await client.finish_order(operation_id=operation_id)
            return "OK"  # OrderManaged(response='1', operation_id=551166)
    except CantFinishOrder:
        return "CantFinishError"
    except WrongOperationID:
        return "WrongOperationError"
    except TryAgainLater:
        return "TryAgainLater"



async def get_phone(api_token:str,service: str, country: int) -> None:
    async with OnlineSMS(api_token) as client:
        api_token = '5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67'
        if service == "ebay":service = "eBay|Kleinanzeigen."
        elif service == "vkontakte":service="vkcom"
        try:order = await client.order_number(service=service, country=country, number=True)
        except NoNumber:return "NoAvailableNumber"
        except NotEnoughFunds:return "NotEnoughFunds"
        return order

# a = asyncio.run(get_phone(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', service='yandex', country="39")) # 2 is a country id received from get_services method.

async def get_sms(api_token:str,operation_id: int) -> None:
    async with OnlineSMS(api_token) as client:

        api_token = '5B8xfqLL4838ft6-HfZbpzK1-NAHxE1z6-J68R39tG-JTfThxPk7ZRuC67'
        my_orders = await client.get_order_info(operation_id=operation_id) # Get Orders
        order = my_orders.orders # Get First Order
        return order.pop()
# asyncio.run(get_sms(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', operation_id=))
  