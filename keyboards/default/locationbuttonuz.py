from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboardUz = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍Manzilni yuborish",
                                                      request_location=True)
                                   ]
                               ])
