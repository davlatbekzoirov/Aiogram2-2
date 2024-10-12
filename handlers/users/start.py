import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import buttons
from time import sleep
from data.config import ADMINS
from loader import dp, db, bot,balance
from aiogram.dispatcher import FSMContext
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    name = message.from_user.full_name
    user_id = message.from_user.id
    try:
        user_get = await bot.get_chat(message.from_user.id)
        user_bio = user_get.bio    
        db.add_user(id=message.from_user.id,fullname=message.from_user.full_name,username=message.from_user.username)
        count = db.count_users()[0]
        await bot.send_message(chat_id='-1002077533723',text=f"""
🆕 Новый пользователь!
🆔 Идентификатор пользователя: {message.from_user.id}
📛 Пользователь: {message.from_user.get_mention()}
🌐 Имя пользователя: {message.from_user.username}
📍 Биография пользователя: {user_bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Итого: {count}""")
    except sqlite3.IntegrityError as err:pass
    # Foydalanuvchini bazaga qo'shamiz
    user_balance = balance.get_balance(user_id=user_id)
    
    await message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>

‼️ЕСЛИ ВАМ НУЖНЫ ЛЮБЫЕ ДРУГИЕ СЕРВИСЫ - ОБРАЩАЙТЕСЬ СЮДА @ser4iksupport ‼️""",reply_markup=buttons)

@dp.callback_query_handler(text="check_subs")
async def checked(call:types.CallbackQuery):
    await call.message.answer("✅ Ваша подписка подтверждена, и вы можете воспользоваться возможностями бота.Нажмите /start")