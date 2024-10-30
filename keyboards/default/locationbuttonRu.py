from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboardRu = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍 Отправить адрес",
                                                      request_location=True)
                                   ]
                               ])
