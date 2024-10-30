from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contactuz = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
    [
        KeyboardButton(text="📲 Raqamni yuborish",request_contact=True)
    ]
])

contactru = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
    [
        KeyboardButton(text="📲 Отправить номмер",request_contact=True)
    ]
])

UzRu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="🇺🇿 O'zbek tili", callback_data="uz"),
        KeyboardButton(text="🇷🇺 Русский язык", callback_data="ru"),
    ]
])