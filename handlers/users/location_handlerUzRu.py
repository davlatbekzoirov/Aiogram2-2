from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.locationbuttonuz import *
from keyboards.default.locationbuttonRu import *
from utils.misc.get_distanceUzRu import *
from loader import dp


@dp.callback_query_handler(text="mylocationUz")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Lokasiya yuboring:", reply_markup=keyboardUz)

@dp.message_handler(content_types='location')
async def get_contactUz(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortestUz(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"<i>Rahmat.</i> \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
        
@dp.callback_query_handler(text="mylocationRu")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Отправить местоположение:", reply_markup=keyboardRu)

@dp.message_handler(content_types='location')
async def get_contactRu(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortestRu(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Расстояние: {distance:.1f} км."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"<i>Спасибо.</i> \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])

