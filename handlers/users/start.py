import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    count = db.count_users()
    try:
        user_get = await bot.get_chat(message.from_user.id)
        user_bio = user_get.bio  
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        await bot.send_message(chat_id='-1002077533723',text=f"""
🆕 Новый пользователь!
🆔 Идентификатор пользователя: {message.from_user.id}
📛 Пользователь: {message.from_user.get_mention()}
🌐 Имя пользователя: {message.from_user.username}
📍 Биография пользователя: {user_bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Итого: {count}""")
        
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    name = message.from_user.full_name
    user_id =message.from_user.id

    photo_id = "AgACAgIAAxkBAAIJ2WXxzr8gV-sXJHHV5ke8Edg6bpwVAAKn1zEbBuWRSw2mx-Dc45NoAQADAgADeQADNAQ"
    msg = f"✋<b>Assalomu alaykum </b>{name},<i>Microsoft Academyning botiga xush kelibsiz</i>\n"
    msg += f"✋<b>Привет, </b>{name}!<i>Добро пожаловать в бот Microsoft Academy</i>"
    await message.answer_photo(photo_id, caption=msg, reply_markup=menu)

    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
