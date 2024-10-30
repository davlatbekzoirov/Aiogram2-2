from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from keyboards.inline.tags import *
from loader import dp, bot

@dp.message_handler(Command('tags'))
async def show_tags(message: types.Message):
    tags_message = """Format: #tag (a'zolar soni).

#python(235), #django(180), #algoritm(149), #oop(113), #pip(103), #web(102), #deploy(99), #import(97), #math(95), #sql(94)

⚠️ Yuqorida eng ko'pida 10 dona tag ko'rsatildi. Hamma taglarni ko'rish va taglarga a'zo bo'lish, a'zolikni bekor qilish uchun 'Tag dashboard'ga o'ting."""
    await message.answer(tags_message, reply_markup=tag, parse_mode=types.ParseMode.MARKDOWN)
