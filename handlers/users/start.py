from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3, logging
from loader import *

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        await db.add_user(name=full_name,id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz")
    except sqlite3.IntegrityError:
        await message.answer("Assalomu alaykum, qayta xush kelibsiz!")
    except Exception as e:
        await message.answer("Xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.")
        logging.exception(f"Error in bot_start handler: {e}")