from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.contacturu import UzRu
import sqlite3
from loader import *
from data.config import ADMINS, CHANNELS
from keyboards.inline.subscription import check_button
from utils.misc import subscription
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    try:
        user_get = await bot.get_chat(message.from_user.id)
        user_bio = user_get.bio    
        dbstart.add_userStart(id=message.from_user.id,fullname=message.from_user.full_name,username=message.from_user.username)
        count = dbstart.count_usersStart()
        await bot.send_message(chat_id='-1002077533723',text=f"""
🆕 Новый пользователь!
🆔 Идентификатор пользователя: {message.from_user.id}
📛 Пользователь: {message.from_user.get_mention()}
🌐 Имя пользователя: {message.from_user.username}
📍 Биография пользователя: {user_bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Итого: {count}""")
    except sqlite3.IntegrityError as err:
        pass
    
    # channels_format = str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     invite_link = await chat.export_invite_link()
    #     # logging.info(invite_link)
    #     channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    # await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
    #                      f"{channels_format}",
    #                      reply_markup=check_button,
    #                      disable_web_page_preview=True)

# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id,
#                                           channel=channel)
#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
#                        f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

#     await call.message.answer(result, disable_web_page_preview=True)

    name = message.from_user.full_name
    user_id =message.from_user.id

    photo_id = "AgACAgIAAxkBAAIJ2WXxzr8gV-sXJHHV5ke8Edg6bpwVAAKn1zEbBuWRSw2mx-Dc45NoAQADAgADeQADNAQ"
    msg = f"✋<b>Assalomu alaykum </b>{name},<i>Microsoft Academyning botiga xush kelibsiz</i>\n"
    msg += f"✋<b>Привет, </b>{name}!<i>Добро пожаловать в бот Microsoft Academy</i>"
    await message.answer_photo(photo_id, caption=msg, reply_markup=UzRu)

# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def bot_start(message: types.Message):
#     await message.reply(message.photo[-1].file_id)