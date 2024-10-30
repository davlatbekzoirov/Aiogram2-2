from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callbackUz, course_callbackRu


# UzRu = InlineKeyboardMarkup(
#     inline_keyboard=[
#     [
#         InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="uz"),
#         InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="ru"),
#     ]
# ])

coursesMenuuz = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari", callback_data=course_callbackUz.new(item_name="pythonuz"))
    ],
    [
        InlineKeyboardButton(text="🌐 Django Web Dasturlash", callback_data=course_callbackUz.new(item_name="djangouz"))
    ],
    [
        InlineKeyboardButton(text="🤖 Mukammal Telegram bot", callback_data="course:telegramuz")
    ],
    [
        InlineKeyboardButton(text="📈 Ma'lumotlar Tuzilmasi va Algoritmlar", callback_data="course:algorithmuz")
    ],
    [
        InlineKeyboardButton(text="📍 Bizning manzil", callback_data="mylocationUz"),
    ],
    [
        InlineKeyboardButton(text="🏘 Boshga qaytish", callback_data="cancel")
    ],
])

coursesMenuru = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🐍 Основы программирования на Python", callback_data=course_callbackRu.new(item_name="pythonru"))
    ],
    [
        InlineKeyboardButton(text="🌐 Веб-программирование на Django", callback_data=course_callbackRu.new(item_name="djangoru"))
    ],
    [
        InlineKeyboardButton(text="🤖 Идеальный Telegram-бот", callback_data="course:telegramru")
    ],
    [
        InlineKeyboardButton(text="📈Структура данных и алгоритмы", callback_data="course:algorithmru")
    ],
    [
        InlineKeyboardButton(text="📍 Наш адрес", callback_data="mylocationRu"),
    ],
    [
        InlineKeyboardButton(text="🏘 В начало", callback_data="cancel")
    ],
])

canceluz = InlineKeyboardMarkup(row_width=1)
back_button = InlineKeyboardButton(text="🏘 Boshga qaytish", callback_data="cancel")
canceluz.insert(back_button)

cancelru = InlineKeyboardMarkup(row_width=1)
back_button = InlineKeyboardButton(text="🏘 В начало", callback_data="cancel")
cancelru.insert(back_button)